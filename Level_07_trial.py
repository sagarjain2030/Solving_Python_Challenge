''' 
In challenge 7, we can see and image. 
We save it as "oxygen.png" 
Looking at source code,there is nothing.
It means we need to work with image itself.
So let's download image and open it with openCV.
Looking closely at image, the middle line of image
has some gray scale dark and light colors.
So if we read image in gray scale format,
and extract middle line, we may get some hint.
''' 
import cv2
img = cv2.imread("oxygen.png", cv2.IMREAD_GRAYSCALE)
print(img.shape)
# here middle line would be 95 //2 , 629 
middle_line = img[img.shape[0] // 2] 
print(middle_line) 
''' 
Looking at middle line after first 115, 
each next element comes exactly for 7 times.
So we take 4th element (zero indexing) and 
then from 5th element, every 7th element 
''' 
middle_filtered_line = []
middle_filtered_line.append(middle_line[4]) 
index = 4 
for i in range(5, len(middle_line)+1, 7): 
	if(middle_line[i] == middle_line[i+1]):
		middle_filtered_line.append(middle_line[i]) 
	else: 
		index = i 
		break 
index += 1 
new_middle = [] 
for index in range(index, len(middle_line)):
	new_middle.append(middle_line[index])
print(middle_filtered_line,len(middle_filtered_line))
for num in middle_filtered_line: 
	print("".join(chr(num)),end="") 
print() 
''' 
Here we get the output : 
smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121] 
so answer would be converting above list into chr 
''' 
answer_list = [105, 110, 116, 101, 103, 114, 105, 116, 121] 
for ans in answer_list: 
	print("".join(chr(ans)), end="") 
print() 
''' 
The answer we got is 'integrity'.
Replacing oxygen with integrity we solve the challenge 
'''