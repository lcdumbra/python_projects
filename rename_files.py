import os
import re

def rename_files():
    file_list = os.listdir(r"C:\Users\ADMIN\Documents\Python Scripts\Udacity\prank")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir(r"C:\Users\ADMIN\Documents\Python Scripts\Udacity\prank")
    for file_name in file_list:
        print("Old Name - " + file_name)
        print("New Name - " + re.sub('[0-9]', '', file_name))
        os.rename(file_name, re.sub('[0-9]', '', file_name))
    os.chdir(saved_path)

rename_files()
