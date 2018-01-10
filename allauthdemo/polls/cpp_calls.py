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

def combpk(parameter, pks):
    return call_process("combpk", parameter, pks)
def addec(ciphers, m):
    return call_process("addec", ciphers, m)
def tally(param, addec_cipher, dec, m):
    return call_process("tally", param, addec_cipher, dec, m)

def call_process(*args):
    call = []
    call.append(os.getcwd() + '/demos_cpp')
    call.extend(args)
    print(call);
    process = subprocess.Popen(call, stdout=subprocess.PIPE)
    out, err = process.communicate()
    #if (args[0] == "combpk"):
        #return " ".join(call)
    return out.decode('utf-8')
