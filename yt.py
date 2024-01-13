import logging
from pytube import YouTube
import random

from local import *


logging.basicConfig(level=logging.INFO)

def download(link: str):
    name = f"{random.randint(100000000, 999999999)}.mp4"

    try:
        yt = YouTube(link)
        title = yt.title
        yt = yt.streams.get_highest_resolution()
        yt.download(filename=name, output_path=PATH)
        
        return title, name
    
    except:
        return "", ""
        