import os
import shlex
import subprocess
import json
import urllib2

#change this file name etc., temporary change to get it working for the meantime
def param(num):
    jsondict = json.load(urllib2.urlopen('http://localhost:8080/param'))
    return json.dumps(jsondict)

def combpk(amount, pks):
    url = 'http://localhost:8080/cmpkstring'
    querystring = '?number='+str(amount)
    for pk in pks:
        querystring += '&PK='+pk

    print(url+querystring)
    jsondict = json.load(urllib2.urlopen(url+querystring))
    print(json.dumps(jsondict))
    return json.dumps(jsondict)

def addec(amount, ciphers):
    url = 'http://localhost:8080/addec'
    querystring = '?number='+str(amount)
    c1s = ciphers['c1s']
    c2s = ciphers['c2s']
    for i, value in enumerate(c1s):
        querystring += "&C1="+str(c1s[i])
        querystring += "&C2="+str(c2s[i])

    print(url+querystring)
    jsondict = json.load(urllib2.urlopen(url+querystring))
    print(json.dumps(jsondict))
    return json.dumps(jsondict)

def tally(param, addec_cipher, dec, m):
    return call_process("tally", param, addec_cipher, dec, m)