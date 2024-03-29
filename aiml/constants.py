'''
Some general-purpose constants, including Python3/Python2 discrimination
'''
import sys

# Package version
VERSION = '0.9.2'

# Python 2/3 compatibility
PY3 = sys.version_info.major == 3
if PY3:
    unicode = str

