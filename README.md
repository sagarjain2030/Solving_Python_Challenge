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


---

## 🔍 Level 3: Hidden Letter Surrounded by Capital Letters

### 🧩 Challenge:
The image shows 7 candles — 3 large on each side, 1 small in the center.  
The page hint reads:  
> "One small letter, surrounded by EXACTLY three big bodyguards on each of its sides."

Nothing in the visible webpage stands out — but the hint and page title (“re”) suggest we need **regex** and to inspect the **page source**.

---

### 🧠 Idea:
In the HTML source, there’s a huge block of noisy characters.  
We’re looking for a **lowercase letter surrounded by exactly 3 uppercase letters on both sides**.  

Pattern to match:
```
AAAxAAA
```
Where:
- `A` = uppercase letter  
- `x` = the hidden lowercase letter we need

This matches regex:  
`[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]`

From each match, we extract the **center lowercase letter**.

### 🐍 Python Solution (Using `requests`, `BeautifulSoup`, and `re`):
```python
import requests
from bs4 import BeautifulSoup
import re

url = "http://www.pythonchallenge.com/pc/def/equality.html"
resp = requests.get(url)

if resp.status_code == 200:
    soup = BeautifulSoup(resp.text, "html.parser")
    messy_block = str(soup.contents[-2])

    pattern = re.compile(r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]')
    matches = re.findall(pattern, messy_block)

    middle_char_regex = re.compile(r'[A-Z]([a-z])[A-Z]')
    for match in matches:
        print(''.join(middle_char_regex.findall(match)), end='')
```

📤 Output:
```
linkedlist
```

🔗 Final Answer:  
👉 http://www.pythonchallenge.com/pc/def/linkedlist.html  
(The page then redirects to: `linkedlist.php`)  
👉 Final URL: http://www.pythonchallenge.com/pc/def/linkedlist.php

---

## Level 4: Follow the Chain
### Challenge:
Image shows a metal chain

Page title: "follow the chain"

No obvious clues on the page itself — but clicking on the image redirects you to:

http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
That page displays:

and the next nothing is 44827
### 🧠 Idea:
We're being asked to follow the nothing parameter in the URL.

Start with nothing=12345

Each page returns a new number in the form:
"and the next nothing is <number>"

We repeatedly follow the chain by updating the URL with this number.

Occasionally, the site says things like:
"Yes. Divide by two and keep going."
In that case, we divide the number and try again.

Eventually, we reach a message with something like: "peak.html" → that’s our answer.

### Python Solution (Loop + Regex):
``` python
import requests
import re

def follow_chain(start_nothing: str):
    base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    url = base_url + start_nothing
    count = 0

    while True:
        resp = requests.get(url)
        if resp.status_code != 200:
            print("❌ Failed to fetch:", url)
            break

        text = resp.text.strip()
        print(f"{count:03}: {text}")  # Show response from each step

        # Case 1: Standard pattern → "next nothing is 12345"
        match = re.search(r"next nothing is (\d+)", text)
        if match:
            url = base_url + match.group(1)
            count += 1
            continue

        # Case 2: Final destination → ends in ".html"
        match = re.search(r"([a-zA-Z]+)\.html", text)
        if match:
            final_url = f"http://www.pythonchallenge.com/pc/def/{match.group(1)}.html"
            print(f"\n🎯 Final URL found: {final_url}")
            break

        # Case 3: Needs manipulation → e.g., divide by 2
        match = re.search(r"(\d+)", text)
        if match:
            divided = str(int(match.group(1)) // 2)
            print(f"⚠️  Dividing and trying again with: {divided}")
            url = base_url + divided
            count += 1
        else:
            print("❓ No valid pattern found. Stopping.")
            break

if __name__ == "__main__":
    follow_chain("12345")
```
### 📤 Output (Partial):
000: and the next nothing is 44827  
001: and the next nothing is 45439  
...
137: Yes. Divide by two and keep going.  
...
250: peak.html

### 🔗 Final Answer:
👉 http://www.pythonchallenge.com/pc/def/peak.html

---

## Level 5: peak hell → Pickle Hell
### 🧩 Challenge:
The title is: “peak hell”

No visible content on the page, but the phrase “peak hell” sounds like “pickle”, a Python module for serialization.

Let’s inspect the page source.

On visiting:

http://www.pythonchallenge.com/pc/def/peak.html

We find a custom HTML tag:

<peakhell src="banner.p"></peakhell>
This strongly suggests we should fetch banner.p and try unpickling it using the pickle module.

### 🧠 Idea:
banner.p seems to be a pickled (serialized) Python object.

We’ll load and unpickle the content.

Upon inspection, it appears to be a list of lists containing (char, repeat_count) tuples.

Reconstructing these as strings will likely reveal the answer in ASCII-art form.

### Python Solution (Using requests + pickle):
```
import requests
import pickle

# Step 1: Start at the original challenge page
page_url = "http://www.pythonchallenge.com/pc/def/peak.html"
resp = requests.get(page_url)

if resp.status_code != 200:
    raise Exception(f"❌ Failed to fetch challenge page: {resp.status_code}")

print("[INFO] Visited peak.html — found reference to banner.p")

# Step 2: Fetch the pickled data file
pickle_url = "http://www.pythonchallenge.com/pc/def/banner.p"
resp = requests.get(pickle_url)

if resp.status_code != 200:
    raise Exception(f"❌ Failed to download pickle file: {resp.status_code}")

print("[INFO] Successfully downloaded banner.p")

# Step 3: Load the pickled data
data = pickle.loads(resp.content)

# Step 4: Each row is a list of (char, count) → reconstruct strings
for row in data:
    line = "".join(char * count for char, count in row)
    print(line)
```
### 📤 Output:
```
  
              #####                                                                      #####  
               ####                                                                       ####  
               ####                                                                       ####  
               ####                                                                       ####  
               ####                                                                       ####  
               ####                                                                       ####  
               ####                                                                       ####  
               ####                                                                       ####  
      ###      ####   ###         ###       #####   ###    #####   ###          ###       ####  
   ###   ##    #### #######     ##  ###      #### #######   #### #######     ###  ###     ####  
  ###     ###  #####    ####   ###   ####    #####    ####  #####    ####   ###     ###   ####  
 ###           ####     ####   ###    ###    ####     ####  ####     ####  ###      ####  ####  
 ###           ####     ####          ###    ####     ####  ####     ####  ###       ###  ####  
####           ####     ####     ##   ###    ####     ####  ####     #### ####       ###  ####  
####           ####     ####   ##########    ####     ####  ####     #### ##############  ####  
####           ####     ####  ###    ####    ####     ####  ####     #### ####            ####  
####           ####     #### ####     ###    ####     ####  ####     #### ####            ####  
 ###           ####     #### ####     ###    ####     ####  ####     ####  ###            ####  
  ###      ##  ####     ####  ###    ####    ####     ####  ####     ####   ###      ##   ####  
   ###    ##   ####     ####   ###########   ####     ####  ####     ####    ###    ##    ####  
      ###     ######    #####    ##    #### ######    ###########    #####      ###      ######  
```
	    
ASCII output spells: channel

### 🔗 Final Answer:
👉 http://www.pythonchallenge.com/pc/def/channel.html

---
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

