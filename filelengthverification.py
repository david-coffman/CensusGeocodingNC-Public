# -*- coding: utf-8 -*-
"""
filelengthverification.py
Created on 2019-07-06 at 10:31
(C) David Coffman 2019

This is proprietary software that may not be redistributed for any reason without written-in-paper authorization from 
the author.
"""

import os

geocoded_directory_path = "/Users/davidcoffman/Documents/PyProjects/CensusGeocodingNC/raw/geocoded/"

for k in os.listdir(geocoded_directory_path):
    if k != ".DS_Store":
        geocoded = open(geocoded_directory_path+k, 'r', errors = 'ignore')
        raw = open("/Users/davidcoffman/Documents/PyProjects/CensusGeocodingNC/raw/"+k, 'r', errors = 'ignore')

        gccount = 0.0
        rawcount = 0.0

        line = "-"
        while line != "":
            line = geocoded.readline()
            gccount += 1

        line = "-"
        while line != "":
            line = raw.readline()
            rawcount += 1

        print("File "+k+": "+str(gccount)+"/"+str(rawcount)+" ("+str(gccount/rawcount)+")")
        if (gccount/rawcount < 0.8) | (gccount/rawcount > 1.0):
            print("WARNING!! ^^^^")

