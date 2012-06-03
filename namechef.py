# 
# Author: Koraa
# Email:  karo@cupdev.net
# Date:   6/1/2012
# 
# This file is licensed under the CC0 licens (Public Domain).
# See the CC0 license under http://creativecommons.org/publicdomain/mark/1.0/
#
# This file is is not intendet to be clean code (would be nice though). Shut up.
#

from time import *
from random import *

import Ice, sys
import Murmur

##################################################
# Init

Ice.loadSlice("-I/usr/share/Ice/slice/ /usr/share/Ice/slice/Murmur.ice")
prop = Ice.createProperties(sys.argv)
prop.setProperty("Ice.ImplicitContext", "Shared")
idd = Ice.InitializationData()
idd.properties = prop
ice = Ice.initialize(idd)
ice.getImplicitContext().put("secret", "secureme")
meta = Murmur.MetaPrx.checkedCast(ice.stringToProxy("Meta:tcp -h 127.0.0.1 -p 6502"))
server=meta.getServer(1)

##################################################
# Funs

def nset(user, serv, name, delay=0.1):
    user.name=name
    serv.setState(user)
    sleep(delay)

def reverse(l):
    last = len(l) -1
    r = []
    for i in xrange(0, len(l)):
        r.append(l[ last -i ])
    return r

birange = lambda a, b : range(a, b) + reverse(range(a+1, b+1))

cpop = lambda s : s[0:len(s) -1]

##################################################
# Funs

def toggle(user, serv, a, b, sleep=0.1):
    while True:
        nset(user, serv, a, sleep)
        nset(user, serv, b, sleep)

def obey(oname, user, serv):
    toggle(user, serv, oname, "(" + oname + ") Ich gehorche dir, nateomus.", 1)

def blink(oname, user, serv, sleep=0.1):
    toggle(user, serv, oname, "", sleep)

def cursor(oname, user, serv, cursor="_", sleep=0.3):
    toggle(user, serv, oname, oname + cursor, sleep)

def PENIS(oname, user, serv, sleep=0.3):
    toggle(user, serv, "8===D", "8======D o o o", sleep)

def emerge(oname, user, serv, delay=0.4):
    s = ["_"] * len(oname)
    ran = range(0, len(oname))
    shuffle(ran)
    for i in ran:
        s[i] = oname[i]
        nset(user, serv, "".join(s), 1.0)

def bounce(oname, user, serv):
    spaceno=18
    for fr in birange(0, spaceno) * 1000:
        nset(user, serv, "[" + (" " * fr) + oname  + (" " * (spaceno - fr)) + "]", 0.08)

def play(oname, user, serv, addtext):
    s = ""
    for i in xrange(0, len(addtext)):
        c = addtext[i]
        if c == "\b":
            s = cpop(s)
        elif c == "\r":
            s = ""
        else:
            s += c

        if i % 2:
            u = "_"
        else:
            u = ""

        nset(user, serv, s + u, randrange(100, 500, 1) / 1000.0)

def kawboom(oname, user, serv):
    play(oname, user, serv, " $ del C:\b\b\b\b\b\bman del\b\b\b\b\b\b\bman rm\b\b\b\b\b\brm -Rf /\r-- BOOM --")
