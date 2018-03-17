import os
import shlex
import subprocess
import json
import urllib2

#change this file name etc., temporary change to get it working for the meantime
def param(num):
    #return call_process("param", num)
    jsondict = json.load(urllib2.urlopen('http://localhost:8080/param'))
    return json.dumps(jsondict)

def combpk(amount, pks):
    url = 'http://localhost:8080/cmpkstring'
    i = 0
    querystring = '?number='+str(amount)
    for pk in pks:
        querystring += '&PK='+pk
        i+=1

    print(url+querystring)
    jsondict = json.load(urllib2.urlopen(url+querystring))
    print(json.dumps(jsondict))
    return json.dumps(jsondict)
def addec(ciphers, m):
    return call_process("addec", ciphers, m)
def tally(param, addec_cipher, dec, m):
    return call_process("tally", param, addec_cipher, dec, m)