"""
Step 1: Understanding the Clues

- Title: "peak hell"
  Sounds like: "pickle"  a hint toward Python's `pickle` module.

- On visiting the page, there's nothing visibly useful.
  So let's inspect the raw HTML using BeautifulSoup and see if we find a clue.
"""

import requests
from bs4 import BeautifulSoup

# Fetch the HTML of the challenge page
page_url = "http://www.pythonchallenge.com/pc/def/peak.html"
resp = requests.get(page_url)

if resp.status_code != 200:
    raise Exception(f"Failed to fetch the challenge page: {resp.status_code}")

# Parse HTML to find hidden hints
soup = BeautifulSoup(resp.text, 'html.parser')
print("[INFO] Raw HTML contents:\n", soup.prettify())

"""
Step 2: Interpreting the HTML

From the soup output, we notice this tag:
<peakhell src="banner.p"></peakhell>

That looks like a custom tag (not standard HTML).
It contains a `src` attribute pointing to a file named `banner.p`.

Maybe this is the file we need to load and deserialize using pickle.
Let's fetch that file next.
"""

# Construct URL for banner.p file
pickle_url = "http://www.pythonchallenge.com/pc/def/banner.p"

# Fetch the pickle file
resp = requests.get(pickle_url)

if resp.status_code != 200:
    raise Exception(f"Failed to fetch pickle file: {resp.status_code}")

print("[INFO] Successfully downloaded banner.p")

"""
Step 3: Unpickling the Data

Time to use the `pickle` module to load this serialized Python object.
We'll inspect what kind of data it holds.
"""

import pickle

# Deserialize the pickle data
data = pickle.loads(resp.content)

# Print first few lines for inspection
print("[INFO] Sample output after unpickling:")
for i, row in enumerate(data[:5]):
    print(f"Row {i}: {row}")

"""
🧵 Step 4: Interpreting the Structure

Each row in the data is a list of (character, count) tuples.

Example:
[(' ', 4), ('#', 2), (' ', 4)] → means: "    ##    "

Let’s now loop over all rows and render the final result visually.
"""

# Render the full ASCII art
for row in data:
    line = "".join(char * count for char, count in row)
    print(line)
"""
Final Step: Interpreting the Output

The printed output reveals a word written in ASCII art:

    channel

That means the next level is at:
http://www.pythonchallenge.com/pc/def/channel.html
"""