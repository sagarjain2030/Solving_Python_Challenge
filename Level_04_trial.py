'''
In challange 4, we have given an image.
And title says : follow the chain.
It means there must be some chaining happening
Now if we click on image, we go to this url:
'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
and it says 'and the next nothing is 44827'
This means we need to keep doing nothing=value
'''
import requests
from bs4 import BeautifulSoup,  NavigableString
import re
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
index_url = 0
while True:
    resp = requests.get(url)
    if(resp.status_code == 200):
        soup = BeautifulSoup(resp.text,'html.parser')
        reg1 = re.compile("next nothing is ([0-9]+)")
        reg2 = re.compile("[0-9]+")
        reg3 = re.compile('([A-Za-z]+).html')
        for content in soup.contents:
            print(content)
            if isinstance(content, NavigableString):
                match = re.findall(reg1,content)
                if(len(match) > 0):
                    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + match[0]
                    index_url += 1
                    print(index_url, " : " ,url)
                else:
                    match = re.findall(reg3,content)
                    if(len(match) > 0):
                        print("http://www.pythonchallenge.com/pc/def/" + match[0] + ".html")
                        url = ""
                        break
                    else:
                        match = re.findall(reg2,url)
                        for m in match:
                            url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(int(match[0])//2)
'''
Running for a while after about 250 urls, you will received output url as :
http://www.pythonchallenge.com/pc/def/peak.html
'''

