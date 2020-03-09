# -*- coding: utf-8 -*-
"""
multithreadedSearcher.py
Created on 2019-07-02 at 17:18
(C) David Coffman 2019

This is proprietary software that may not be redistributed for any reason without written-in-paper authorization from 
the author.
"""

import censusgeocode
import csv
import sys
import io
import os
import threading

basefilepath = "/Users/davidcoffman/Documents/PyProjects/CensusGeocodingNC/raw/"
temp_path = "/Users/davidcoffman/Documents/PyProjects/CensusGeocodingNC/raw/tmp/"

def geocode_district(districtIdentifier):

    # Split into manageable pieces.
    infile = basefilepath + districtIdentifier + ".txt"
    infile = open(infile, 'r',errors='ignore')

    tempfilename = temp_path + "0.csv"
    tempfile = open(tempfilename, 'w+')

    line = infile.readline()
    line = infile.readline()
    linenum = 1

    while line != "":
        if linenum % 10000 == 0:
            tempfile.close()
            tempfilename = temp_path + str(int(linenum/10000)) + ".csv"
            tempfile = open(tempfilename, 'w+')

        line = line.replace("	"," ")
        line = line[1:-2]
        split = line.split('" "')
        id = int(split[2])
        address = split[13].strip()
        city = split[14]
        zip = split[16].strip()
        if address != "REMOVED":
            tempfile.write(",".join([str(id),address,city,"NC",zip])+"\n")
        linenum += 1
        line = infile.readline()
    tempfile.close()

    print("Stage one complete: "+districtIdentifier)

    outfile = open(basefilepath +"geocoded/" + districtIdentifier + ".txt", "w+")

    threads = []

    for k in os.listdir(temp_path):
        if k != ".DS_Store":
            if k != "geocoded.txt":
                threads.append(threading.Thread(target=threadedSearch, args=[k,outfile]))


    # for k in threads:
    #     k.start()
    # for k in threads:
    #     k.join()

    while (len(threads) > 5):
        for k in threads[0:5]:
            k.start()
        for k in threads[0:5]:
            k.join()
        threads = threads[5:]
    for k in threads:
        k.start()
    for k in threads:
        k.join()

    outfile.close()

    for k in os.listdir(temp_path):
        if k != ".DS_Store":
            if k != "geocoded.txt":
                os.remove(temp_path+k)

def threadedSearch(k,outfile):
    cg = censusgeocode.CensusGeocode(benchmark="9")
    rettype = "locations"
    infile = temp_path + k
    result = cg.addressbatch(infile, returntype=rettype, timeout=600)
    fieldnames = cg.batchfields[rettype] + ['lat', 'lon']
    fieldnames.pop(fieldnames.index('coordinate'))
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    # writer.writeheader()
    writer.writerows(result)
    print("File processing complete: "+k)

for k in range(91,101):
    geocode_district("ncvoter"+str(k))
