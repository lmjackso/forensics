
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
# script to register Python 2.0 or later for use with win32all
# and other extensions that require Python registry settings
#
# Adapted by Ned Batchelder from a script
# written by Joakim Low for Secret Labs AB / PythonWare
#
# source:
# http://www.pythonware.com/products/works/articles/regpy20.htm
 
import sys
 
from _winreg import *
 
# tweak as necessary
version = sys.version[:3]
installpath = sys.prefix
 
regpath = "SOFTWARE\\Python\\Pythoncore\\%s\\" % (version)
installkey = "InstallPath"
pythonkey = "PythonPath"
pythonpath = "%s;%s\\Lib\\;%s\\DLLs\\" % (
    installpath, installpath, installpath
)
 
def RegisterPy():
    try:
        reg = OpenKey(HKEY_LOCAL_MACHINE, regpath)
    except EnvironmentError:
        try:
            reg = CreateKey(HKEY_LOCAL_MACHINE, regpath)
        except Exception, e:
            print "*** Unable to register: %s" % e
            return
 
    SetValue(reg, installkey, REG_SZ, installpath)
    SetValue(reg, pythonkey, REG_SZ, pythonpath)
    CloseKey(reg)
    print "--- Python %s at %s is now registered!" % (version, installpath)
 
if __name__ == "__main__":
    RegisterPy()