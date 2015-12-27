# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 14:19:55 2015

@author: steve
"""
import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_194073.xml'
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
#print data
tree = ET.fromstring(data)
counter = 0
tot = 0
for elem in tree.iter():
    if elem.tag == 'count':
        counter += 1
        tot += int(elem.text)
print "Count: ",counter
print "Sum:  ", tot
        