from PIL import Image
import os

fpath = '../dataset/code'

def verifyImages(folder_path):
    for path, subdirs, files in os.walk(folder_path):
        counter=0
        for name in files:
            file_path = os.path.join(path,name)
            try:
                im = Image.open(file_path)
                im.verify() #I perform also verify, don't know if he sees other types o defects
                im.close() #reload is necessary in my case
            except Exception as e: print(e)
            

verifyImages(fpath)
