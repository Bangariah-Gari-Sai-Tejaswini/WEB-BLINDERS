#!/usr/bin/env python
# coding: utf-8

# 1.Write a Python program to reverse a string.
# 
# input : hellohowareyoudoingandhowisyourhealth

# In[1]:


# write your code here
s=input()
print(s[::-1])


# 2.Write a Python program to capitalize the first letter of each word in a sentence.
# 
# input : hello welcome to internship

# In[2]:


# write your code here
s=input()
print(s.title())


# 3.Write a Python program to find the longest word in a sentence.
# 
# input : "he is very good at painting and paint good sketches"

# In[5]:


# write your code here
s=input()
lw=0
for word in s.split(" "):
    lw=len(word) if len(word)>lw else lw
print(lw)


# 4.Write a Python program to find the length of the last word in a sentence.
# 
# input : this is the most beautiful beach I ever visited

# In[6]:


# write your code here
s=input()
words=s.split()
print(len(words[-1]))


# 5.Write a Python program to find the second most frequent character in a string.
# 
# input: the hospital is very big and this hospital has so many doctors

# In[11]:


# write your code here
from collections import Counter
s=input()
freq = Counter(s.replace(" ",""))
sorted_f = sorted(freq.items(),key = lambda x: x[1],reverse=True)
if len(sorted_f)>1 :
    print(sorted_f[1][0])


# In[ ]:




