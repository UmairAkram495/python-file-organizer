import os
import shutil

os.chdir(r"c:/Users/Abc/Desktop/Python/File")
folder_path = "c:/Users/Abc/Desktop/Python/File"
for item in os.listdir(folder_path):
    full_path=os.path.join(folder_path,item)
    if os.path.isfile(full_path):
        print(item)
        _ ,extension=os.path.splitext(full_path)
        e= extension.lower()
        video_extensions = {".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv", ".webm", ".mpeg"}
        if (e==".jpg" or e== ".jpeg" or e== ".png" or e== ".webp" or e== ".gif" or e== ".heic" or e== ".bmp" or e== ".tiff"):
            shutil.move(full_path,"c:/Users/Abc/Desktop/Python/File/Images")
        elif e in video_extensions:
            shutil.move(full_path, "c:/Users/Abc/Desktop/Python/File/Videos")
        elif e == ".pdf":
            shutil.move(full_path, "c:/Users/Abc/Desktop/Python/File/PDFs")
        else:
            shutil.move(full_path, "c:/Users/Abc/Desktop/Python/File/Others")
