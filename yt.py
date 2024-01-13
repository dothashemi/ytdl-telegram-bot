import configparser
import random
import yt_dlp

from local import *


def download(link: str):
    file_name = random.randint(100000000, 999999999)

    options = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f'{PATH}{file_name}.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(link, download=True)
            video_title = info.get('title', 'Untitled Video')

            print(f'Title: {video_title}')

            return video_title, f"{file_name}.mp4"
    
    except:
            return "Failed!", "Failed!"