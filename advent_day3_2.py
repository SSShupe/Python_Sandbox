# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
data = open('/home/steve/Downloads/input_3.txt').read()
data = data.strip()
santa = []
robosanta = []
for i, char in enumerate(data):
    if i % 2 == 0:
        santa.append(char)
    else: robosanta.append(char)
    
santa_visited = [(0,0)]
start = [0,0]
for i in santa:        
    if i == '>':
        start[0] += 1
    elif i == '<':
        start[0] -= 1
    elif i == '^':
        start[1] += 1
    else:
        start[1] -= 1
    santa_visited.append(tuple(start))

robosanta_visited = [(0,0)]
start = [0,0]
for i in robosanta:        
    if i == '>':
        start[0] += 1
    elif i == '<':
        start[0] -= 1
    elif i == '^':
        start[1] += 1
    else:
        start[1] -= 1
    robosanta_visited.append(tuple(start))
all_visited = santa_visited + robosanta_visited
unique = set(all_visited)
print(len(unique))


            
        
