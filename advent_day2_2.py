# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
data = open('/home/steve/Downloads/input_3.txt').read()
data = data.strip()
visited = [[0,0]]
start = [0,0]
for i in data:    
    if i == '>':
        start[0] += 1
    elif i == '<':
        start[0] -= 1
    elif i == '^':
        start[1] += 1
    else:
        start[1] -= 1
    visited.append(start)
    start = start
print(head(visited))

            
        
