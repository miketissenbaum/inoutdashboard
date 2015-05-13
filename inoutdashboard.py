#!/usr/bin/python:

import bluetooth
import time
import json
from json import dumps, load

print "In/Out Board"

m = 0
p = 0

while True:
    print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())

    result = bluetooth.lookup_name('AD:35:AF:4D:83:7C', timeout=5)
    if (result != None):
        m = "In"
        print "Mike: in"
    else:
        m = "Out"
        print "Mike: out"

    result = bluetooth.lookup_name('04:6D:77:C0:1F:42', timeout=5)
    if (result != None):
        p = "In"
        print "Adam: in"
    else:
        p = "Out"
        print "Adam: out"


    with open("text.json", "w") as file:
        json.dump({'Mike':m, 'Adam':p}, file, indent=4) 
    time.sleep(60)

with open("test") as file:
    result = load(file)
print (type(result))
print (result.keys())
print (result)
