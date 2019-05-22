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