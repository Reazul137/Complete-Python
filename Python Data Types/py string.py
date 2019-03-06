# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 11:41:08 2019

@author: Md Reazul Islam
"""

s = 'Hello world!'

# s[4] = 'o'
print("s[4] = ", s[4])

# s[6:11] = 'world'
print("s[6:11] = ", s[6:11])

#generates error
#strings are immutable in python

s[5]='d'