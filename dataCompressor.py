# -*- coding: utf-8 -*-
"""
dataCompressor.py
Created on 2019-07-03 at 21:15
(C) David Coffman 2019

This is proprietary software that may not be redistributed for any reason without written-in-paper authorization from 
the author.
"""

import os
import csv

geocoded_directory = "/Users/davidcoffman/Documents/PyProjects/CensusGeocodingNC/raw/geocoded/"
compressed_directory = "/Users/davidcoffman/Documents/PyProjects/CensusGeocodingNC/raw/geocompressed/"

for k in os.listdir(geocoded_directory):
    if k != ".DS_Store":
        infile = open(geocoded_directory+k, 'r', errors='ignore')
        outfile = open(compressed_directory+k,'w+')
        csvreader = csv.reader(infile, delimiter=',', quotechar='"')
        csvwriter = csv.writer(outfile, delimiter=',', quotechar='"')
        for k in csvreader:
            if k[2] == "True":
                csvwriter.writerow([k[0],k[7],k[8]," "])

        infile.close()
        outfile.close()

