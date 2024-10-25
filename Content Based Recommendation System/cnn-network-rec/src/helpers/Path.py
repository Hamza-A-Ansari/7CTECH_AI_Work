import os



def full_path(path):
    # Base path
    BASE_PATH=os.getcwd()

    f_path = f"{BASE_PATH}{path}"


    return f_path