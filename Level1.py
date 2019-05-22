# -*- coding: utf-8 -*-
"""
Created on Wed May 22 22:26:42 2019

@author: Sagar
"""
def convert(cipherText):
    plainText = ""
    for c in cipherText:
        #  If Character is Neither
        if(not str.isalpha(c)):
            plainText += c
        #  If Character is UpperCase
        elif(str.isupper(c)):
            plainText += chr(((ord(c) - ord('A') + key) % 26) + ord('A'))
        # if Character is LowerCase
        else:
            plainText += chr(((ord(c) - ord('a') + key) % 26) + ord('a'))
            
    return plainText


key = 2
cipherText = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print(convert(cipherText))

print("Applying on url")
cipherText = "map"
print(convert(cipherText))