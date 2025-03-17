#!/usr/bin/env python
# coding: utf-8

# *** USE THE CONCEPT OF FUNCTIONS TO SOLVE THE BELOW PROGRAMMING QUESTIONS ***

# 1) Write a Python function that accepts a string and counts the number of upper and lower case letters.
# 
# Sample String : 'The quick Brow Fox'
# 
# Expected Output :
# 
# No. of Upper case characters : 3
# 
# No. of Lower case Characters : 12

# In[3]:


#WRITE YOUR CODE HERE
def check(s):
    uc=0
    lc=0
    for ch in s:
        if ch.isupper():
            uc+=1
        elif ch.islower():
            lc+=1
    return uc,lc
s = input()
uc,lc=(check(s))
print("No. of Upper case characters : ",uc)
print("No. of Lower case characters : ",lc)


# 2) Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# 
# Sample List : [1,2,3,3,3,3,4,5]
# 
# Unique List : [1, 2, 3, 4, 5]

# In[11]:


#WRITE YOUR CODE HERE
def u1(a):
    return list(set(a))
a=list(map(int,input().split()))
print(sorted(u1(a)))


# 3) Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
# 
# Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.

# In[18]:


#WRITE YOUR CODE HERE
def checkp(n):
    if n<1 :
        return False
    for i in range(2,int(n**0.5) +1,1):
        if n%i==0 :
            return False
    return True
n = int(input())
res=checkp(n)
print("yes prime" if res else "not prime")


# 4)Write a Python program to print the even numbers from a given list.
# 
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 
# Expected Result : [2, 4, 6, 8]
# 

# In[19]:


# WRITE YOUR CODE HERE
def e1(a):
    evn1=list(filter(lambda x:x%2==0,a))
    return evn1
a = list(map(int,input().split()))
print(e1(a))


# 5) Write a Python function to check whether a string is a pangram or not.
# 
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# 
# For example : "The quick brown fox jumps over the lazy dog"

# In[7]:


# WRITE YOUR CODE HEREfddddddddddddd
def is_pangram(s):
    return set(string.ascii_lowercase) <= set(s.lower())
s=input()
if is_pangram :
    print("yes")
else:
    print("no")


# 
