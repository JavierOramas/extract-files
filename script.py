import zipfile
import shutil
import os
import typer
from os import path

app = typer.Typer()

ext = ['.mpeg','.mp4','.avi','.mpg','.3gp','.webm', '.mov', '.mkv','.wmv', '.vob', '.ogg', '.ogv']

def is_video(f):
    for i in ext:
        if(f.lower().endswith(i)):
            return True
    return False

@app.command(name='extract',help='extracts all videos in [Source Folder] to [Destination Folder]')
def extract_videos(source:str, dest_folder:str):
    
    os.makedirs('../'+dest_folder,exist_ok=True)
    for cp,dir,files in os.walk(source):
        for f in files:
            if is_video(f):
                os.makedirs(path.join('../'+dest_folder,cp[2:]),exist_ok=True)
                shutil.move(path.join(cp,f),path.join('../'+dest_folder,cp[2:]))

# extract_videos(source_folder,dest_folder)                

if __name__ == "__main__":
    app()