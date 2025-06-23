from src.lib.Libraries import *
from controller.prerequisite import data_model_loader
from controller.summarization import summarizer
from controller.dump_data import dumping_db

def main():

    tokenizer_model, fetch_product_ids, existing_data, product_tags, tags_to_exclude  = data_model_loader()

    if not fetch_product_ids == 0:
        updated_results = summarizer(tokenizer_model, fetch_product_ids, existing_data, product_tags, tags_to_exclude)

        if not updated_results == 0:
            dumping_db(updated_results)


if __name__=='__main__':
    main()