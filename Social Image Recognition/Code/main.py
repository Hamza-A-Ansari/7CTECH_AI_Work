from controller.phase_one import category_prediction
from controller.phase_two import tags_prediction
from controller.phase_three import final_prediction
from controller.post import post_results
from controller.delete import delete_image

def main(id, endpoint):
    
    server_response = "Prediction unsuccessful"
    log_key = f"id {id} endpoint {endpoint} "

    image_pil, category_response, insta_image_path = category_prediction(endpoint, log_key)

    if category_response != 0:

        cat_df = tags_prediction(image_pil, category_response, log_key)

        if not cat_df.empty:

            results_list = final_prediction(cat_df, image_pil, log_key)

            post_results(id, results_list, log_key)

            delete_image(insta_image_path, log_key)

            return results_list

        else:
            try:
                delete_image(insta_image_path)
                return server_response
            except:
                return server_response

    else:
        try:
            delete_image(insta_image_path)
            return server_response
        except:
            return server_response

    

if __name__=='__main__':
    main(404, '3455306946419482864.n.jpg')