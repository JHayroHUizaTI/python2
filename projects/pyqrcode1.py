import pyqrcode

import os, shutil

title = input("Give your QR code a title!!! ")
text = input("What would you like the QR code to say? ")

file_name_png = title + ".png"

url = pyqrcode.create(text)

url.png(file_name_png, scale=8)

os.mkdir(fr"/home/whoami/Documents/project_vscode/python/projects/qrs/{title}")

shutil.move(f"{file_name_png}", fr"/home/whoami/Documents/project_vscode/python/projects/qrs/{title}")