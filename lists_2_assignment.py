#!/usr/bin/env python
# coding: utf-8

# 1.Remove empty strings from the list1 of strings
# 
# list1 = ["Mike", " ", "Emma", "Kelly", " ", "Brad"]
# 
# 
# 

# In[1]:


# write your code here
list1 = ["Mike", " ", "Emma", "Kelly", " ", "Brad"]
filtered_list = [item for item in list1 if item.strip()]
print(filtered_list)


# 2.Write a program to add item 7000 after 6000 in the following Python List
# 
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# 
# expected o/p ; [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

# In[2]:


#  write your code here
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)


# 3.You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.
# 
# list1 = [5, 10, 15, 20, 25, 50, 20]
# 
# Expected output:
# [5, 10, 15, 200, 25, 50, 20]

# In[5]:


list1 = [5, 10, 15, 20, 25, 50, 20]
idx = list1.index(20)  # Use 'idx' instead of 'index'
list1[idx] = 200
print(list1)


# 4.Remove all occurrences of a specific item from a list.
# Given a Python list, write a program to remove all occurrences of item 20.
# 
# list1 = [5, 20, 15, 20, 25, 50, 20]
# 
# Expected output:
# 
# [5, 15, 25, 50]

# In[6]:


# write your code here
list1 = [5, 20, 15, 20, 25, 50, 20]
filtered_list = [item for item in list1 if item != 20]
print(filtered_list)


# 5.Concatenate two lists in the following order
# 
# list1 = ["Hello ", "take "]
# 
# list2 = ["Dear", "Sir"]
# 
# Expected output:
# 
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

# In[ ]:


# write your code here
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
concatenated_list = [a + b for a in list1 for b in list2]
print(concatenated_list)

