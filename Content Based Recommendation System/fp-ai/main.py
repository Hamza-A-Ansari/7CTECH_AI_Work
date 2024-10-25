# from src.training.old_Train import * 
# from src.validation.old_val import *
from src.training.Train import * 
from src.validation.val import * 
from src.uploading.upload import *



def main():

    print("Train Funtion")

    train()

    print("Valid Funtion")

    val()

    print("upload function")

    upload()
    print("uploaded csv")

    print("complete")



if __name__ == '__main__': 

    main()