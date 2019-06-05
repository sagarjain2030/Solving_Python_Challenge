# Solving_Python_Challenge
The python challege is kind of online Treasure hunt where one need to use the programming skills to solve (actually to ease) the level.Even though its quite possible to solve levels in programming language, it has been created to use python as prefereble language.
The link to begin challenge is [here](http://www.pythonchallenge.com/)
So let's begin:

### Level 0:
Consider the level as starting point for programming knowledge.It has a picture with written over picture as 2^38^. The hint given is "Try chaning url."
So lets first calculate 2^38^.  
Once calculated, we will replace zero in url with that value.  
That's it.   
The answer url is http://www.pythonchallenge.com/pc/def/274877906944.html

### Level 1:
The level consist of cipher text which need to be decrypt to reach next level. The hint given as K - M, O -> Q , E -> G. This is nothing but ceaser cipher. Now, from given hint, the key is obviously 2. 
Now data is all small letters and some symbols, which no need to replace. Solving for given string will give us hint to apply same for url.Applying the resulting string will be 
http://www.pythonchallenge.com/pc/def/ocr.html

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