# -*- coding: utf-8 -*-
"""
multithreadedDownloader.py
Created on 2019-07-03 at 13:22
(C) David Coffman 2019

This is proprietary software that may not be redistributed for any reason without written-in-paper authorization from 
the author.
"""

import requests
import threading

urlbase = "https://s3.amazonaws.com/dl.ncsbe.gov/data/"

def get_district(num):
    url1 = urlbase+"ncvoter"+str(num)+".zip"
    url2 = urlbase+"ncvhis"+str(num)+".zip"
    data1 = requests.get(url1)
    data2 = requests.get(url2)
    print("Done with "+str(num))
    f = open('/Users/davidcoffman/Documents/PyProjects/CensusGeocodingNC/raw/ncvoter'+str(num)+".zip", 'wb')
    f.write(data1.content)
    f.close()
    f = open('/Users/davidcoffman/Documents/PyProjects/CensusGeocodingNC/raw/ncvhis'+str(num)+".zip", 'wb')
    f.write(data2.content)
    f.close()

threads = []

for num in range(1,101):
    threads.append(threading.Thread(target=get_district,args=[num]))

for k in threads:
    k.start()

for k in threads:
    k.join()

print("Done!")