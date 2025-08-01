"""
Level 4: Follow the Chain
-------------------------
Clue from the page:
    - Image of a chain
    - Page title: "follow the chain"

When you click on the image, you're redirected to:
    http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345

That page says:
    "and the next nothing is 44827"

So clearly, this is a linked chain of numbers — we have to follow the `nothing=` parameter and extract the next number repeatedly.
"""

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
        print(f"{count:03}: {text}")  # Show response from each link

        # Case 1: Regular next link
        match = re.search(r"next nothing is (\d+)", text)
        if match:
            next_nothing = match.group(1)
            url = base_url + next_nothing
            count += 1
            continue

        # Case 2: Final message contains something.html
        match = re.search(r"([a-zA-Z]+)\.html", text)
        if match:
            final_url = f"http://www.pythonchallenge.com/pc/def/{match.group(1)}.html"
            print(f"\n🎯 Final URL found: {final_url}")
            break

        # Case 3: Unexpected message (e.g., "Yes. Divide by two and keep going.")
        match = re.search(r"(\d+)", text)
        if match:
            divided_nothing = str(int(match.group(1)) // 2)
            print(f"⚠️ Dividing and trying again with: {divided_nothing}")
            url = base_url + divided_nothing
            count += 1
        else:
            print("❓ No match found in response. Stopping.")
            break

if __name__ == "__main__":
    follow_chain("12345")
