"""
Level 2: Finding the Rare Characters
------------------------------------
Clue from the page:
    - Image of an open book
    - Hint: "recognize the characters. maybe they are in the book,
             but MAYBE they are in the page source."

Goal:
    - Look into the page source (HTML) for hidden characters.
    - Find rare alphabetic characters in a large block of noise.
"""

import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    """
    Sends a GET request to the URL and returns the parsed HTML content.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        raise Exception(f"Failed to fetch page. Status code: {response.status_code}")

def extract_hidden_text(soup):
    """
    Extracts the large hidden text block from the soup and returns only alphabetic characters.
    """
    # Optional: Save raw content for manual inspection (for educational clarity)
    with open("Level_02_raw_dump.txt", 'w') as f:
        for part in soup.contents:
            f.write(str(part))

    # Observation: The mess of characters is near the bottom of the page's body
    # Typically found in the second last element
    text_block = str(soup.contents[-2])

    # Filter and collect only alphabetic characters
    filtered = ''.join([ch for ch in text_block if ch.isalpha()])
    return filtered

def main():
    url = "http://www.pythonchallenge.com/pc/def/ocr.html"
    soup = fetch_html(url)
    
    answer = extract_hidden_text(soup)
    
    print("🔎 Extracted Answer from Page Source:")
    print(answer)
    
    print("\n🌐 New URL:")
    print(f"http://www.pythonchallenge.com/pc/def/{answer}.html")
    # Output: http://www.pythonchallenge.com/pc/def/equality.html

if __name__ == "__main__":
    main()
