# -*- coding: utf-8 -*-
"""
Created on Sat May 25 20:13:53 2019

@author: Sagar
"""
import re

s = ''.join([line.rstrip() for line in open('InputLevel3.txt')])
result = re.findall("[a-z]{1,}[A-Z]{3}([a-z])[A-Z]{3}[a-z]{1,}",s)
print(result)


