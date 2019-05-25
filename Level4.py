# -*- coding: utf-8 -*-
"""
Created on Sat May 25 20:54:36 2019

@author: Sagar
"""
import urllib.request as agent
import re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
dynamicData = "12345"
i = 0
finalResult = ""
while True:
    i += 1 
    print("The current iteration is : {}".format(i),end = " ")
    s =  agent.urlopen(url + dynamicData)
    pattern = "the next nothing is ([\d]+)"
    text = str(s.read())
    print(text)
    possibleSwitch = "Divide by two and keep going"
    if(possibleSwitch in text):
        dynamicData = str(int(dynamicData) // 2)
    else:
        result = re.findall(pattern,text)
        if(len(result) > 0):
            dynamicData = result[0]
        else:
            finalResult = text
            break
    
print(finalResult)