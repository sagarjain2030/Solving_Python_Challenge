# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 14:40:41 2019

@author: Sagar
"""
from PIL import Image

img =  Image.open("oxygen.png")
(width, height)  = (img.width,img.height)
row = [(x,height//2) for x in range(width)]

s = []
for r in row[::7]:
    s.append(chr((img.getpixel(r))[0]))

print("".join(s))
newList = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for x in newList:
    print(chr(x),end="")
    
