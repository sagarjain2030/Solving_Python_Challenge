# -*- coding: utf-8 -*-
"""
Created on Sat May 25 21:58:59 2019

@author: Sagar
"""

import urllib.request as agent
import pickle


link = agent.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(link)
for dataInstance in data:
    print("".join(character * num for character,num in dataInstance))
