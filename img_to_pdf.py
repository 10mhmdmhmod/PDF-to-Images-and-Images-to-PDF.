from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askdirectory
import os

Tk().withdraw()
user_imgs_path = askdirectory()
list_imgs = os.listdir(user_imgs_path)
full_paths = [user_imgs_path+"/"+ n for n in list_imgs]

imgs_read = [Image.open(path) for path in full_paths]
conv_imgs_rgb = [ img.convert("RGB") for img in imgs_read]
first_bag = [conv_imgs_rgb[0]]
all_after_first = conv_imgs_rgb[1:]

Tk().withdraw()
save_path = askdirectory()
pdf_name = input("Enter pdf name : ")
reso_lution =float(input("Enter Resolution : "))
first_bag[0].save(save_path+"/"+pdf_name+".pdf",resolution=reso_lution,save_all=True, append_images=all_after_first)