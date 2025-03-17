#!/usr/bin/env python
# coding: utf-8

# *** USE THE CONCEPT OF FUNCTIONS TO SOLVE THE BELOW PROGRAMMING QUESTIONS ***

# 1) Write a Python function to sum all the numbers in a list.
# 
# Sample List : (8, 2, 3, 0, 7)
# 
# Expected Output : 20
# 

# In[6]:


#WRITE YOUR CODE HERE
def s1(a):
    return sum(a)
a = list(map(int,input("Sample List : ").split()))
print(s1(a))


# 2) Write a Python function to multiply all the numbers in a list.
# 
# Sample List : (8, 2, 3, -1, 7)
# 
# Expected Output : -336

# In[9]:


#WRITE YOUR CODE HERE
def m1(a):
    res=1
    for i in a:
        res = res*i
    return res
    
a = list(map(int,input("Sample List : ").split()))
print(m1(a))


# 3) Write a Python program to reverse a string.
# 
# Sample String : "1234abcd"
# 
# Expected Output : "dcba4321"

# In[11]:


#WRITE YOUR CODE HERE
def r1(s):
    return s[::-1]
s = input()
print(r1(s))


# 4) Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

# In[1]:


#WRITE YOUR CODE HERE
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
num = int(input())
if num<0:
    print("hey stop")
else:
    print(fact(num))


# 5) Write a Python function to check whether a number falls within a given range.

# In[4]:


#WRITE YOUR CODE HERE
def check(s,e,n):
    if n<=e and n>=s:
        print("yes,falls in range")
    else:
        print("no")
s,e,n = list(map(int,input("enter start and end and number : ").split()))
check(s,e,n)


# In[ ]:




