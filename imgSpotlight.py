# Working ✔✔✔

import shutil
import os
import tempfile
from tkinter import filedialog

print("###   #     #  #####           #####")
print(" #    ##   ## #     #         #     #  #          #     ####   #    #   #####")
print(" #    # # # # #               #        #          #    #    #  #    #     #")
print(" #    #  #  # #  ####  #####   #####   #          #    #       ######     #")
print(" #    #     # #     #               #  #          #    #  ###  #    #     #")
print(" #    #     # #     #         #     #  #          #    #    #  #    #     #")
print("###   #     #  #####           #####   ######     #     ####   #    #     #")

path = "C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\".format(
    username=os.getlogin()
)

def findSpotlight():
    with tempfile.TemporaryDirectory() as tmp_dir:
        for file in os.listdir(path):
            if not os.path.isfile(path + file):
                continue
            if (os.stat(path + file).st_size / 1024) < 400:
                continue
            shutil.copy(path + file, tmp_dir)

        for file in os.listdir(tmp_dir):

            if file + ".jpg" in os.listdir(tmp_dir):
                os.remove(tmp_dir + file)
                continue
            if not os.path.splitext(file)[1] == ".jpg":
                os.rename(tmp_dir + "\\" + file, tmp_dir + "\\" + file + ".jpg")

        if not len(os.listdir(tmp_dir)) == 0:
            dest_dir = filedialog.askdirectory()
            if not dest_dir:
                print("Please select a folder!")
                return
            for file in os.listdir(tmp_dir):
                shutil.copy(tmp_dir + "\\" + file, dest_dir)
            print("The images were saved to {}".format(dest_dir))
            print("\033[96m{}\033[00m".format("Done!"))
        else:
            print("\033[91m{}\033[00m".format("No images found!"))
findSpotlight()
