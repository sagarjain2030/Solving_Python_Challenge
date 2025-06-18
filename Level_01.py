"""
Level 1: Simple Caesar Cipher
-----------------------------
Clue from the image:
    K -> M
    O -> Q
    E -> G

Hint:
    "Everybody thinks twice before solving this."

Observation:
    - Each character seems to be shifted by +2 in the alphabet.
    - This is a simple Caesar cipher.
    - We test both forward (+2) and backward (-2) translations.

Goal:
    Decrypt the given text and extract the next URL path.
"""

def translate_forward(input_string):
    """
    Shifts each alphabetical character forward by 2.
    Non-alphabet characters are left unchanged.
    """
    output = ''
    for ch in input_string:
        if ch.isalpha():
            if ch in ['y', 'z']:
                # Wrap around the alphabet for 'y' and 'z'
                output += chr(ord(ch) - 24)
            else:
                output += chr(ord(ch) + 2)
        else:
            output += ch
    return output

def translate_backward(input_string):
    """
    Shifts each alphabetical character backward by 2.
    Non-alphabet characters are left unchanged.
    """
    output = ''
    for ch in input_string:
        if ch.isalpha():
            if ch in ['a', 'b']:
                # Wrap around the alphabet for 'a' and 'b'
                output += chr(ord(ch) + 24)
            else:
                output += chr(ord(ch) - 2)
        else:
            output += ch
    return output

def main():
    input_text = (
        "g fmnc wms bgblr rpylqjyrc gr zw fylb. "
        "rfyrq ufyr amknsrcpq ypc dmp. "
        "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. "
        "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. "
        "lmu ynnjw ml rfc spj."
    )

    # Apply forward translation (+2 shift)
    decoded_text = translate_forward(input_text)
    print("Decoded Message (Forward Shift):\n")
    print(decoded_text)
    print("\n" + "="*60 + "\n")

    # Apply backward translation (-2 shift) just for comparison
    reversed_text = translate_backward(input_text)
    print("Reversed Message (Backward Shift - for comparison):\n")
    print(reversed_text)
    print("\n" + "="*60 + "\n")

    # Suggested by the decoded text: use str.maketrans() for URL transformation
    print("Translating URL part 'map' using maketrans:")

    from_str = "abcdefghijklmnopqrstuvwxyz"
    to_str   = "cdefghijklmnopqrstuvwxyzab"
    cipher_table = str.maketrans(from_str, to_str)

    url_part = "map"
    translated_url_part = url_part.translate(cipher_table)

    print(f"'map' ➜ '{translated_url_part}'")

    print("\nNew URL: http://www.pythonchallenge.com/pc/def/ocr.html")

if __name__ == "__main__":
    main()
