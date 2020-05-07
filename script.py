import zipfile
import shutil
import os
from os import path

def extract_videos(source:str):
    
    os.makedirs('../Music_Videos',exist_ok=True)
    
    for cp,dir,files in os.walk(source):
        for f in files:
            # print(f)
            if f.endswith('.mpeg') or f.endswith('.mp4') or f.endswith('.avi') or f.endswith('.mpg'or f.endswith('.3gp'or f.endswith('.MOV')or f.endswith('.webm')or f.endswith('.MOV')or f.endswith('.mkv'))):
                os.makedirs(path.join('../Music_Videos',cp[2:]),exist_ok=True)
                # print(path.join('../Videos',cp[2:]))
                shutil.move(path.join(cp,f),path.join('../Music_Videos',cp[2:]))

        # for cp,dir,files in os.walk(destination):
        #     for f in files:

extract_videos('.')                
