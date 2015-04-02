# coding: utf-8

import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['C:\\Users\\ernest\\Documents\\scripts\\introducingPython'])
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0])
letters[1]
letters[-1]
letters[-2]
letters[25]
letters[5]
letters[100]
name = 'Henry'
name[0] = 'P'
name.replace('H', 'P')
'P' + name[-1]
'P' + name[1:]
