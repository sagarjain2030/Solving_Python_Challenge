"""
Level 3: Hidden Character Between Capital Patterns
--------------------------------------------------

Clue from the page:
    - Image shows 7 candles: 3 large on each side, 1 small in the center.
    - Hint: "One small letter, surrounded by EXACTLY three big bodyguards on each of its sides."

Goal:
    - View the page source (HTML) and extract the long string of characters.
    - Use regex to find lowercase letters surrounded by exactly 3 uppercase letters on both sides.
    - Combine all such lowercase letters to reveal the answer.
"""

import requests
from bs4 import BeautifulSoup
import re   

def fetch_html_content(url):
    """
    Fetch the HTML content of the given URL and return the parsed soup object.
    """
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        raise Exception(f"Failed to fetch page. Status code: {response.status_code}")

def extract_encoded_text(soup):
    """
    Writes the soup content to a file (for inspection) and returns the relevant raw text block.
    """
    with open("level_03_raw_dump.txt", 'w') as f:
        for part in soup.contents:
            f.write(str(part))
    
    # The long string of mixed characters is near the bottom
    return str(soup.contents[-2])

def extract_hidden_letters(data):
    """
    Uses regex to find the pattern described in the hint:
    One small letter, surrounded by EXACTLY 3 uppercase letters on each side.
    """
    # Main pattern: lowercase surrounded by 3 uppercase letters on both sides
    pattern = re.compile(r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]')
    matches = re.findall(pattern, data)

    # From each match, extract the middle lowercase character only
    extract_center = re.compile(r'[A-Z]([a-z])[A-Z]')
    for match in matches:
        center = re.findall(extract_center, match)
        for c in center:
            print(c, end='')

def main():
    url = "http://www.pythonchallenge.com/pc/def/equality.html"
    soup = fetch_html_content(url)
    encoded_data = extract_encoded_text(soup)
    extract_hidden_letters(encoded_data)

    # Output: linkedlist
    print("\n\n🌐 New URL: http://www.pythonchallenge.com/pc/def/linkedlist.html")
    print("📍 Hint from next page: It redirects to 'linkedlist.php' — so use:")
    print("➡️ Final URL: http://www.pythonchallenge.com/pc/def/linkedlist.php")

if __name__ == "__main__":
    main()