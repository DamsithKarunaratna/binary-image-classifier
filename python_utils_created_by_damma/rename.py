import os

fpath = './notCode'

def replace(folder_path):
    for path, subdirs, files in os.walk(folder_path):
        counter=0
        for name in files:
            file_path = os.path.join(path,name)
            extension = os.path.splitext(file_path)[1]
            # new_name = os.path.join(path,name.lower().replace(old,new))
            new_name = os.path.join(path,"{:08d}{}".format(counter, extension))
            os.rename(file_path, new_name)
            counter = counter + 1

replace(fpath)