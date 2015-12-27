# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 17:12:39 2015

@author: steve
"""

s = open('/home/steve/Downloads/input.txt').read()
counter = 0
position = 0

for char in s:
    if counter < 0:
        print position
        break
    else:
        if char == '(':
            counter += 1
            position += 1
        elif char == ')':
            counter -= 1
            position += 1

        