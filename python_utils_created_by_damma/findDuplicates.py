from PIL import Image
from PIL import ImageStat
import os

fpath = './oop'
fileObjects = []
unique_hash_list = [] 
delete_file_list = []    

class MapItem(object):
    def __init__(self, path, value):
        self.path = path
        self.value = value

def hash_image(image_path):
    img = Image.open(image_path).resize((8,8), Image.LANCZOS).convert(mode="L")
    mean = ImageStat.Stat(img).mean[0]
    return sum((1 if p > mean else 0) << i for i, p in enumerate(img.getdata()))

def walk(folder_path):
    cur_hash = 0
    prev_hash = 0
    for path, subdirs, files in os.walk(folder_path):
        for name in files:
            file_path = os.path.join(path,name)
            cur_hash = hash_image(file_path)
            fileObjects.append(MapItem(file_path, cur_hash))
            if(cur_hash == prev_hash):
                os.remove(file_path)
                print('duplicate removed')
            prev_hash = cur_hash
    

walk(fpath)
for obj in fileObjects:
    if obj.value not in unique_hash_list:
        unique_hash_list.append(obj.value)
        print("unique")
    else:
        delete_file_list.append(obj.path)
        print(obj.path)
    print('\n')

for filepath in delete_file_list:
    os.remove(filepath)
    print('IT WAS removed')