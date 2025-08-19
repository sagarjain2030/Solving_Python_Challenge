"""
Python Challenge - Level 7 Solution

In this challenge, we are given an image file `oxygen.png`. 
The hint lies within the image itself rather than the source code.

Steps:
1. Load the image in grayscale using OpenCV.
2. Inspect the middle horizontal line of pixels.
3. Observe that ASCII values are encoded as repeated grayscale values.
4. Extract every 7th pixel after the first few to decode the hidden message.
5. The message provides a list of ASCII codes which decode to the final answer.

Answer: Replace `oxygen` with `integrity` in the URL to proceed.
"""

import cv2

# Step 1: Read the image in grayscale
img = cv2.imread("oxygen.png", cv2.IMREAD_GRAYSCALE)

# Print the shape to understand dimensions (height, width)
print("Image shape:", img.shape)

# Step 2: Extract the middle horizontal line of pixels
middle_line = img[img.shape[0] // 2]
print("Middle line pixel values extracted")

# Step 3: Analyze repeating pattern (each character is repeated ~7 times)
middle_filtered_line = [middle_line[4]]  # Start with the 4th pixel value

for i in range(5, len(middle_line) - 1, 7):
    # Ensure repetition confirms a valid character encoding
    if middle_line[i] == middle_line[i + 1]:
        middle_filtered_line.append(middle_line[i])
    else:
        break

# Step 4: Decode grayscale values into characters
hidden_message = "".join(chr(num) for num in middle_filtered_line)
print("Hidden message:", hidden_message)

# Step 5: Extract ASCII list from message
answer_list = [105, 110, 116, 101, 103, 114, 105, 116, 121]
final_answer = "".join(chr(num) for num in answer_list)

print("Final Answer:", final_answer)

"""
Output:
Hidden message: smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
Final Answer: integrity
"""
