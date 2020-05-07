import zipfile
import shutil
import os
from os import path

ext = ['.mpeg','.mp4','.avi','.mpg','.3gp','.webm', '.mov', '.mkv','.wmv', '.vob', '.ogg', '.ogv']

def is_video(f):
    for i in ext:
        if(f.lower().endswith(i)):
            return True
    return False
def extract_videos(source:str):
    
    os.makedirs('../Music_Videos',exist_ok=True)
    
    
    for cp,dir,files in os.walk(source):
        for f in files:
            # print(f)
            if is_video(f):
                os.makedirs(path.join('../Music_Videos',cp[2:]),exist_ok=True)
                # print(path.join('../Videos',cp[2:]))
                shutil.move(path.join(cp,f),path.join('../Music_Videos',cp[2:]))

        # for cp,dir,files in os.walk(destination):
        #     for f in files:


extract_videos('.')                
