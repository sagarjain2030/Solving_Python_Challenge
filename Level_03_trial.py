'''
In challenge 3, we are given 
Input : Image with 7 candles, 3 big on each side while middle is very small.
Hint : One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.

Now looking at site link, there is nothing like this.
Now if we check page source, there is string of many many characters. 
That means we need to figure out the hint from that string.
Let's just first read the page source.
'''

import requests
from bs4 import BeautifulSoup
import re

def main():
    url='http://www.pythonchallenge.com/pc/def/equality.html'
    #open with GET method
    resp=requests.get(url)
    if resp.status_code==200:
        soup=BeautifulSoup(resp.text,'html.parser')
        # print(soup.contents)
        with open("Level_03_01.txt",'w') as f:
            for data in soup.contents:
                f.write(str(data))
    list_data = soup.contents
    required_data = str(list_data[-2])
    # Now looking at that string, we need to find such character
    # one small character is in between exactly 3 capital letters 
    # on each side.
    # one more hint you can get is from webpage title
    # webpage title for this challenge has text 're'
    # it means we have to use regex.
    reg = re.compile('[a-z][A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]')
    match = re.findall(reg,required_data)
    print(match)
    reg_middle_char = re.compile('[A-Z][a-z][A-Z]')
    for m in match:
        new_match = re.findall(reg_middle_char,m)
        for s in new_match:
            print(s[1],end='')
    # This will give us 'linkedlist'
    # replacing it in url
    # new url will be : http://www.pythonchallenge.com/pc/def/linkedlist.html
    # when you will go to this link, a new page will open saying : 
    # linkedlist.php
    # so change url : http://www.pythonchallenge.com/pc/def/linkedlist.php
    # your challenge is solved.

if __name__ == "__main__":
    main()