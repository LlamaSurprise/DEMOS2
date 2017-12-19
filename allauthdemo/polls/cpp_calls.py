import os
import shlex
import subprocess

def param(num):
    return call_process("param", num)
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
