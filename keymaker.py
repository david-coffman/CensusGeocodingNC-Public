# -*- coding: utf-8 -*-
"""
keymaker.py
Created on 2019-07-06 at 13:26
(C) David Coffman 2019

This is proprietary software that may not be redistributed for any reason without written-in-paper authorization from 
the author.
"""

keyfile = open("/Users/davidcoffman/Desktop/SummerProjects/Swift/DCM/PackageManifest/key.txt", 'w+')

for k in range(1,101):
    voterfile = open("/Users/davidcoffman/Desktop/SummerProjects/Swift/DCM/Raw/ncvoter"+str(k)+".txt", 'r')
    line = voterfile.readline()
    line = voterfile.readline()
    line = line[line.index('"')+1:]
    line = line[line.index('"') + 1:]
    line = line[line.index('"') + 1:]
    this_county = line[:line.index('"')]

    print(this_county)
    keyfile.write(this_county+"\n")
    voterfile.close()

keyfile.close()

