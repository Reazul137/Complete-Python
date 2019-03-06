# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 22:53:22 2019

@author: Md Reazul Islam
"""

t = (5, 'program', 1+3)

#t[1] = 'program'
print("t[1] = ", t[1])

#t[0:3] = (5, 'program', (1+3j))
print("t[0:3]=", t[0:3])

#generates error
#tuples are immutable

t[0] = 10