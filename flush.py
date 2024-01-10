#!/bin/python3

import os
from datetime import datetime, timedelta

from local import *


def flush(directory, extension, age):
    now = datetime.now()
    threshold = now - timedelta(hours=age)

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                modification_time = datetime.fromtimestamp(os.path.getmtime(file_path))

                if modification_time <= threshold:
                    try:
                        os.remove(file_path)
                    except Exception as e:
                        print(f"Error removing file {file_path}: {e}")


extension = '.mp4'
age = 12

flush(PATH, extension, age)
