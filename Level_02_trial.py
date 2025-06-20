# Challenge 02
# Input: Image with open Book
# Hint :recognize the characters. maybe they are in the book,
# but MAYBE they are in the page source.

# this means we have to search in the page source.
# TO get page source we can use libraries requests and beautiful soup

import requests
from bs4 import BeautifulSoup
url='http://www.pythonchallenge.com/pc/def/ocr.html'
    
#open with GET method
resp=requests.get(url)
if resp.status_code==200:
    soup=BeautifulSoup(resp.text,'html.parser')
    # print(soup.contents)
    with open("Level_02_01.txt",'w') as f:
        for data in soup.contents:
            f.write(str(data))
    # now looking at file, we can see there are bunch of characters in second last element of soup.content
    # and above that it is written find rare characters in the mess below:
    # so we need to find characters in that mess
    list_data = soup.contents
    required_data = str(list_data[-2])
    for ch in required_data:
        if(ch.isalpha()):
            print(ch,end='')
    # this will print the word: equality
    # so the new url is : http://www.pythonchallenge.com/pc/def/equality.html


