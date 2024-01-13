import configparser
import random
import yt_dlp

from local import *


def download(link: str):
    file_name = random.randint(100000000, 999999999)

    yt_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
        'outtmpl': f'{PATH}{file_name}.%(ext)s',
    }

    try:
        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            info = ydl.extract_info(link, download=False)
            video_title = info.get('title', 'Untitled Video')

            print(f'Title: {video_title}')

            ydl.download([link])
            
            return video_title, f"{file_name}.mp4"
        
    except:
            return "Failed!", "Failed!"