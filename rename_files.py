import os

def rename_files():
    
    #(1) get file names from a folder
    picture_path = "/Users/danielchang/Python/prank/"
    file_list = os.listdir(picture_path)
    print(file_list)
    
    #(2) for each file, rename filename
    saved_path = os.getcwd()
    os.chdir(picture_path)
    for file_name in file_list:
        os.rename(file_name, file_name.translate(file_name.maketrans('','','0123456789')))
    os.chdir(saved_path)

rename_files()
