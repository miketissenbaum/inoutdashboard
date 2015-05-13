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

    result = bluetooth.lookup_name('BC:F5:AC:5D:93:7C', timeout=5)
    if (result != None):
        m = "In"
        print "Mike: in"
        #return (m)
    else:
        m = "Out"
        print "Mike: out"
        #return(m)

    result = bluetooth.lookup_name('00:61:71:C1:1B:42', timeout=5)
    if (result != None):
        p = "In"
        print "Adam: in"
        #return(p)
    else:
        p = "Out"
        print "Adam: out"
        #return(p)

    result = bluetooth.lookup_name('0C:14:20:0F:27:C3', timeout=5)
    if (result != None):
        c = "In"
        print "Craiggers: in"
        #return(c)
    else:
        c = "Out"
        print "Craiggers: out"
        #return(c)

    result = bluetooth.lookup_name('B8:5A:73:DD:DF:72', timeout=5)
    if (result != None):
        l = "In"
        print "Lauren: in"
        #return(l)
    else:
        l = "Out"
        print "Lauren: out"
        #return(l)

    with open("text.json", "w") as file:
        json.dump({'Mike':m, 'Adam':p, 'Craiggers':c, 'Lauren':l}, file, indent=4) 
    time.sleep(60)

with open("test") as file:
    result = load(file)
print (type(result))
print (result.keys())
print (result)
