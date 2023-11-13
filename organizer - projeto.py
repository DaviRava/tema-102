import os 
import shutil

from_dir = "C:/Users/Pichau/Downloads/"
to_dir = "C:/Users/Pichau/Documents/"

list = os.listdir(from_dir)
print(list)

for file in list:
    name, extension = os.path.splitext(file)
    print(extension)
    if extension in ['.txt','.doc', '.docx', '.pdf']:
        path1 = from_dir + file
        path2 = to_dir + "downloads"
        path3 = to_dir + "downloads/" + file

        if os.path.exists(path2):
            print("movendo arquivo", file)
            shutil.move(path1, path3)
        
        else:
            os.makedirs(path2)
            print("movendo arquivo", file)
            shutil.move(path1, path3)