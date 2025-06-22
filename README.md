# 🧠 Solving Python Challenge

Welcome to my personal walkthrough of the [Python Challenge](http://www.pythonchallenge.com/) — an online puzzle series designed to enhance your problem-solving skills using Python. Each level presents a unique challenge that often involves decoding images, parsing data, or manipulating text.

This repository is my implementation of the challenge with:
- 🧼 Clean, well-commented Python scripts  
- 📚 Use of only necessary libraries  
- 🧰 Proper documentation and tooling  
- 📈 Aiming for clarity, not just completion

---

## 🚀 How to Use This Repo

Each level is solved in its own Python file (`level_00.py`, `level_01.py`, etc.), accompanied by helpful comments explaining the logic and reasoning.

> ✅ **Note**: I solve each puzzle manually before referring to any AI tools or online hints — the goal is skill-building, not just speed.

---

## 🔍 Level 0: 2^38

### 🧩 Challenge:
The page shows an image with the text `2^38`.  
Hint provided: **"Try to change the URL."**

### 💡 Idea:
Compute the value of `2^38` and insert that result into the URL.

### 🐍 Solution (Python):
```python
print(2**38)
```
---
## 🔍 Level 1: Caesar Cipher (2-Shift)

### 🧩 Challenge:
The image shows:  
K → M  
O → Q  
E → G  
And the hint says:  
**"Everybody thinks twice before solving this."**  
You're also given a long encoded message.

### 💡 Idea:
The clue suggests a **Caesar cipher** with a shift of **+2** (i.e., each letter is replaced by the letter two steps forward).  
To decode the text, shift every lowercase letter forward by 2, wrapping around at `'z' → 'a'`.

You can do this manually or use Python’s `str.maketrans()` to build a translation table.

### 🐍 Solution (Python):
```python
from_str = "abcdefghijklmnopqrstuvwxyz"
to_str   = "cdefghijklmnopqrstuvwxyzab"
table = str.maketrans(from_str, to_str)

input_text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. "
        "rfyrq ufyr amknsrcpq ypc dmp. "
        "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. "
        "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. "
        "lmu ynnjw ml rfc spj."
print(input_text.translate(table))
```

🔗 Final Answer:  
Apply the same transformation to the URL "map" → "ocr"
So the next level is:  
👉 http://www.pythonchallenge.com/pc/def/ocr.html


---

## 🔍 Level 2: Hidden Characters in Page Source

### 🧩 Challenge:
The image shows an open book, and the hint reads:  
"recognize the characters. maybe they are in the book,    
but MAYBE they are in the page source."

That strongly suggests that we need to look at the **HTML source code** of the page.


### 🧠 Idea:
On inspecting the source, we find a huge block of noisy characters.  
Just above it, there's another line:  
  **"find rare characters in the mess below."**  
So we filter only the **alphabetic characters** from that mess — those are the meaningful ones.  


### 🐍 Python Solution (Using `requests` and `BeautifulSoup`):
```python
import requests
from bs4 import BeautifulSoup

url = "http://www.pythonchallenge.com/pc/def/ocr.html"
resp = requests.get(url)

if resp.status_code == 200:
    soup = BeautifulSoup(resp.text, "html.parser")
    messy_block = str(soup.contents[-2])
    result = ''.join([ch for ch in messy_block if ch.isalpha()])
    print(result)

```
📤 Output:
equality

🔗 Final Answer:  
👉 http://www.pythonchallenge.com/pc/def/equality.html


### Level 2:
For the next level, we need to dig through source code of webpage. In given webpage source, there is mess of character is given and hint is given as find rarest character.
So using dictionary, we get rarest characters and they form the word "equality". So resultant url become
http://www.pythonchallenge.com/pc/def/equality.html

### Level 3:
For this level, hint given is <i>One small letter, surrounded by EXACTLY three big bodyguards on each of its sides</i>. So, it means exactly 3 capital letters followed by 1 small letter and again followed by 4 capital letters. The data can be found in source code of webpage. 
In previous as well this challenge, we need to clean the input. In previous challenge, input is manually cleaned. In this case, python can be useful to clean it out.   
Now, comes to main part.As per hint, we need to find all possible combination where pattern is as per hint.Since pattern, its better to use Regex. From regex, we get 10 such patterns. Now, if we take only middle lower letter, we get string "linkedlist". Let's try it out.The resultant url become: http://www.pythonchallenge.com/pc/def/linkedlist.html

### Level 4: 
For this level, just look at the source code. The next url will be made such that every new page contains string "next nothing is " and integer value. This integer value needs to be fed to url to get to new page.The requrement is to keep going until the necessary file name in found.    
Remember to look for message since it might have some tweaks and tricks in its sleeves.But till now, I like this challenge and definitely others as well.The resulting url is http://www.pythonchallenge.com/pc/def/peak.html

### Level 5:
This level is not so intuitive.First of all, there is an image and below it is written as "pronounce it". It makes no sense what to pronounce and how to.But if you see source code, name of image is "Peakhill". This can only be decipher if you really knew python libraries. You are like me, you would be having no clue what it means.So I did what we always good at doing.Google it. You will find some links to solutions of challenge but what's fun in that. The hint, however, is good enough.The library is pickel.Pickel is serilization library for serilization and deserilization of data.  
Now, the source code has info of source for peakhell, the url is <i> http://www.pythonchallenge.com/pc/def/banner.p</i> Clicking on link, gives some random data.
Now that we know the library for deserilization, let's fetch the data from above url, just like we did in 4th Challege.Printing data from pickle will result into some tuples of # and spaces.So we need to print tuples in one string format.The output is amazingly printed word "channel." Thus, the resulting url is http://www.pythonchallenge.com/pc/def/channel.html

### Level 6:
Now, there is zipline of jeans shown in image.Going to source code, paypal symbol has nothing to do with challenge. Going line by line in source code, the comment is given as zip. From that and from image, it is obvious that level is related to zip files. Now, since zip is an extension, writing it in url instead of html will give us a zip file.  
Extracting zip file will give multiple files and a README. The readme has 2 hints.one filename where to start looking and other is that answer is in zip file only.Just like Level 4, repetatively open new file,read content find new number and open the new file. After continuing this, last file content suggested to collect and print comment of those files.Printing it, the name received is HOCKEY. But wait, its not the solution. hockey page gives hint as to see letters that form hockey design and the word is Oxygen. http://www.pythonchallenge.com/pc/def/oxygen.html

### Level 7:
Level 7 shows an image with gray line in middle. It is obvious that clue will be in that line.So to read image, Pillow will be better suitable library. Now let's extract middle gray line from image and if we check pixels of middle line,we can see a pattern as RGB values which are same while last value being 255. Also the same pixel tuple is repeated for 7 times. So consider single value from them and ignore the other 6.  
Now, the values can be considered as ASCII values. So converting these values into ASCII, we get the message as "smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]pe_" Similar to pixel values, lets convert the given array into ASCII values which will result in "integrity". Hence the resulting url is http://www.pythonchallenge.com/pc/def/integrity.html

### Level 8:
Level 8 shows an image with selectable bee. On clicking, it will open a dialog box asking for username and password. But where can we find it?  
Lets check out source code. The source code contains clear written un and pwd i.e. username and password. This means we can get username andpassword from it. But before that there is some string written "BZh91AY". Searching on google will tell you that its nothing but  compressed using bzip. Decompressing it, will result in username as huge and password as file. Filling these values will lead to result url as http://www.pythonchallenge.com/pc/return/good.html

### Level 9:
Seeing image, we can remember drawing we used to complete in our childhood where there were dots given and by connecting those dots, we create our drawing.Same thing we need to do here. Checking out the source code, we see two huge length of number arrays. We just need to use those points for drawing. Image will look like cow.So putting cow in url, we get result as its male. So it must be bull. So resulting url will be http://www.pythonchallenge.com/pc/return/bull.html

