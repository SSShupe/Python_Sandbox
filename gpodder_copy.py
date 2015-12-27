# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 06:30:59 2015

@author: steve
"""

import os
import glob
import shutil
mp3s = glob.iglob('*.[Mm][Pp]3')
newest = max(mp3s, key=os.path.getctime)
source = os.listdir("/home/steve/gPodder/")
destination = "/tmp/newfolder/"
for files in source:
    if files == newest:
        shutil.move(files,destination)

for file in os.listdir('/home/steve/gPodder/Downloads'):
    print(os.path.getctime('/home/steve/gPodder/Downloads/' + file))
import datetime
    print(datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S'))