#!/usr/bin/env python
# coding: utf-8

# *** USE THE CONCEPT OF LOOPS TO SOLVE THE BELOW PROGRAMS***

# 1) Python program to count the total number of digits in a number.
# 
# TAKE THE INPUT NUMBER : 123456
# 
# 
# 
# 

# In[1]:


#wRITE YOUR CODE HERE
n=int(input())
print(len(str(n)))


# 2) Python program to count the number of even and odd numbers from a series of numbers.
# 
# num_list = [1,3,5,6,99,134,55]

# In[2]:


#WRITE YOUR CODE HERE
nums = list(map(int,input("Hey enter numbers:").split()))
ec=0
oc=0
for num in nums:
    if(num%2 == 0):
        ec+=1
    else:
        oc+=1
print("odd count:",oc)
print("even count:",ec)


# 3) Python program to get the Fibonacci series between 0 to 50.

# In[6]:


#WRITE YOUR CODE HERE
a=0
b=1
while a<=50:
    print(a,end = " ")
    c=a+b
    a=b
    b=c


# 4) Python program that accepts a string and calculates the number of digits and letters.
# 
# Input
# 
# WEBBLINDERS1234

# In[8]:


#WRITE YOUR CODE HERE
s=input()
d=0
l=0
for char in s:
    if char.isalpha():
        l+=1
    elif char.isdigit():
        d+=1
print("digits",d)
print("letters",l)


# 5) Python program to display all numbers within a range except the prime numbers.
# 
# INPUT RANGE : 30 TO 80

# In[12]:


#WRITE YOUR CODE HERE
def isprime(n):
    if(n<2):
        return False
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False
    return True
for i in range(30,81,1):
    if not isprime(i):
        print(i,end=" ")


# In[ ]:




