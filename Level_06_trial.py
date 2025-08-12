'''
In challenge 6, we have an image of zipper of pant
and a title saying "now there are pairs".
Looking at image , it is clear that we need to handle
zip file.
But where is zip file. 
Let's look at source code. 
In source code, nothing directly given as zip file.
But we have "zip" written as above the head.
it means we need to replace the head of url with zip.
That means, channel.html will become channel.zip
channel.zip gives us a zip file with which we need
to perform operations.
'''
from zipfile import ZipFile
import re


file_name = "channel.zip"
comments = []
with ZipFile(file_name,"r") as zipfile:
    # we first get the list of files
    zipfile.printdir()
    comments.append(zipfile.comment.decode("utf-8"))
    # here we have a readme.txt file
    # Reading it's content will give us some more hints
    # Remember, reading file in zip gives byte stream
    # we need to decode it into utf-8
    with zipfile.open("readme.txt","r") as f:
        data = f.readlines()
        for line in data:
            print(line.decode('utf-8'))
    '''
    readme.txt gives us output as:
    welcome to my zipped list.
    hint1: start from 90052
    hint2: answer is inside the zip
    So we open now file 90052
    '''
    with zipfile.open("90052.txt", "r") as f:
        data = f.readlines()
        for line in data:
            print(line.decode('utf-8'))
    '''
    we see output from file 90052.txt as :
    Next nothing is 94191
    This is similar to level 3 challenge
    which we already solved.
    '''
    '''
    after running we get 
    [b'Next nothing is 46145']
    [b'Collect the comments.']
    In zip files, you can add comment to zipfile itself 
    and also to each file in zipfile.
    That can be taken without extracting zipfile
    So we need to add code first to break the loop at 
    [b'Collect the comments.'] and also collecting
    all comments of the files inside zip file.
    Also the comment of zip file itself.
    '''
    file_number = "90052"
    terminate = False
    while(not terminate):
        file_path = file_number + ".txt"
        with zipfile.open(file_path,"r") as f:
            data = f.readlines()
            print(data)
            comment = zipfile.getinfo(file_path).comment
            comments.append(comment.decode('utf-8'))
            for line in data:
                line = line.decode('utf-8')
                reg1 = re.compile("Next nothing is ([0-9]+)")
                reg2 = re.compile(r"Collect the comments")
                match = re.findall(reg2,line)
                if(len(match) > 0):
                    terminate = True
                    break
                match = re.findall(reg1,line)
                for m in match:
                    file_number = m
print("".join(comment for comment in comments))
'''
we get the output as :
****************************************************************
****************************************************************
**                                                            **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
**   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
**   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
**                                                            **
****************************************************************
 **************************************************************
 which seems hockey.
 So replacing channel.html with hockey.html
 we go to another page which says:
 "it's in the air. look at the letters."
 The letters are : OO OO XX YY GG GG EE NN => OXYGEN
 So replacing channel with OXYGEN
 we solve the challenge.
'''