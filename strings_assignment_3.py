#!/usr/bin/env python
# coding: utf-8

# 1.Write a Python program to count the number of vowels in a string.
# 
# input : hasdfgeuionhjl

# In[1]:


# write your code here
s = input()
v="aeiouAIEOU"
count=sum(1 for ch in s if ch in v)
print(count)
    


# 2.Write a Python program to count the occurrences of each word in a sentence.
# 
# input : hi hello hi and and hi more and more programming

# In[3]:


# write your code here
from collections import Counter
s=input()
words=s.split()
word_c = Counter(words)
for w,c in word_c.items():
    print(w,':',c)


# 3.In python how can you differentiate strings and lists. Give atleast 5 different comparisons between them.

# Answer:

# 4.Write a string for your own of approximately 40 in length and perform any 5 different string operations on that.

# In[4]:


s = "Python programming is fun and interesting!"

print(s.upper())
print(len(s))
print(s.replace("fun", "exciting"))
print(s.count("i"))
print(s[0:6])


# 5.Explain the concatination in strings with a neat example.

# In[4]:


#write your code and explanation here


# In[5]:


s1 = "Hello"
s2 = "World"

result = s1 + " " + s2  # Concatenation using +
print(result)  # Output: Hello World


# In[ ]:




