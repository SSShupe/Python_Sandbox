# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 08:43:06 2015

@author: steve
"""

import os
import glob
import shutil
import itertools
templist = []

for filenames in os.walk('/home/steve/gPodder/Downloads'):
    v = list(filenames)   
    templist.append(v)

chain = list(itertools.chain(*templist))

newest = max(mp3s, key=os.path.getctime)
source = os.listdir("/home/steve/gPodder/")
destination = "/tmp/newfolder/"
for files in source:
    if files == newest:
        shutil.move(files,destination)