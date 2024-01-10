#!/bin/python3

import subprocess
from local import *


command = f"find {PATH}*.mp4 " + "-type f -mtime +0.5 -exec rm {} +"

try:
    result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
except subprocess.CalledProcessError as e:
    print(e.stderr)
