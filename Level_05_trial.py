'''
In challange 5, we have given an image.
And title says : peak hell.
And the hint says : pronounce it
Pronoucing it leads us to new library of python : Pickle
The pickle module in Python provides a way to serialize and deserialize Python object structures.
It means there must be some serialization and deserialization we need to do
There is no object directly seen on webpage.
So we go to url
'http://www.pythonchallenge.com/pc/def/peak.html'
and get the data
If we print the data:
<peakhell src="banner.p"></peakhell>
if we replace peak.html with banner.p, if we get some data. 
so let's try some pickling on it.
'''
import requests
from bs4 import BeautifulSoup
import pickle
url = "http://www.pythonchallenge.com/pc/def/peak.html"
resp = requests.get(url)
if(resp.status_code == 200):
    soup = BeautifulSoup(resp.text,'html.parser')
    print(soup.contents)
'''
We get "<peakhell src="banner.p"></peakhell>"
so our url becomes: "http://www.pythonchallenge.com/pc/def/banner.p"

'''
url = "http://www.pythonchallenge.com/pc/def/banner.p"
resp = requests.get(url)
print(pickle.loads(resp.content))
'''
so now we get list of characters and some number,
which I think will print that character for that number of times.
'''
data = pickle.loads(resp.content)
for d in data:
    print("".join(character * num  for character,num in d))
'''
We get the output "channel"
replacing peak.html with channel.html
'''