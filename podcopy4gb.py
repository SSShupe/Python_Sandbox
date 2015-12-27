# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 12:35:15 2015

@author: steve
"""
import os
import time
import shutil
usbdir = '/run/media/steve/USB4GB/gPodder'
filelist = [f for f in os.listdir(usbdir)]
print("Removing existing podcasts")
for f in filelist:
    fullpath = usbdir + '/' + f
    os.remove(fullpath)
mp3_list = []
print("Copying new podcasts to USB.")
for i in os.walk('/home/steve/gPodder/Downloads'):
    for file in i[2]:
        if file.endswith('.mp3'):
            mp3_list.append(i[0] + '/' + file)
            
now = time.time()
ago = now - 10000
for i in mp3_list:
    statinfo = os.stat(i)
    mtime = statinfo.st_mtime
    if mtime > ago:
        shutil.copy(i, usbdir)
