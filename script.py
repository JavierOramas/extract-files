import zipfile
import shutil
import os
import typer
from os import path

app = typer.Typer()

ext = {}
ext['Video'] = ['.mpeg','.mp4','.avi','.mpg','.3gp','.webm', '.mov', '.mkv','.wmv', '.vob', '.ogg', '.ogv']
ext['Audio'] = [ '.mp3', '.wav', '.aac', '.wma', '.dss', '.dvf', '.m4p', '.midi']
ext['Pictures'] = ['.jpg', '.jpeg', '.png', '.jfif', '.exif', '.tiff', '.gif', '.gif', '.bmp', '.ppm', '.pgm', '.pbm', '.pnm', '.webp', '.heif', '.img', '.ico']

def is_video(f, types):
    for i in ext[types]:
        if(f.lower().endswith(i)):
            return True
    return False

@app.command(name='extract',help='extracts all [file_types] (Videos,Audio,Pictures) in [Source Folder] to [Destination Folder]')
def extract_videos(types:str, source:str, dest_folder:str):
    
    os.makedirs('../'+dest_folder,exist_ok=True)
    for cp,dir,files in os.walk(source):
        for f in files:
            if is_video(f,types):
                os.makedirs(path.join('../'+dest_folder,cp[2:]),exist_ok=True)
                shutil.move(path.join(cp,f),path.join('../'+dest_folder,cp[2:]))
        if len(os.listdir(cp) ) == 0:
            os.rmdir(cp)

# extract_videos(source_folder,dest_folder)                

if __name__ == "__main__":
    app()