# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 09:31:31 2015

@author: steve
"""

import os
import glob
os.chdir('/home/steve/gPodder/Downloads')
newest = max(glob.iglob('*.[Mm][Pp]3'), key=os.path.getctime)