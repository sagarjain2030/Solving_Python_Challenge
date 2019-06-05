# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 13:46:25 2019

@author: Sagar
"""

import zipfile
import re

zipFile = zipfile.ZipFile("channel.zip")
i = 0
num = "90052"
fileName = num + ".txt"
comment = ""
while True:
    content = str(zipFile.read((fileName)))
    comment += str(zipFile.getinfo(fileName).comment.decode('utf-8'))
    pattern = "Next nothing is ([\d]+)"
    result = re.findall(pattern,content)
    i += 1 
    print("The current iteration is : {}".format(i),end = " ")
    print(fileName + " : "+ content)
    
    if(len(result) > 0):
        num = result[0]    
        fileName = num + ".txt"
    else:
        break
print(comment)