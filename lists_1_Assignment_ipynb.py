#!/usr/bin/env python
# coding: utf-8

# 1.Are lists mutable or immutable, explain with an example

# In[1]:


my_list = [1, 2, 3]
print("Original List:", my_list)
#yes they are mutable
my_list[1] = 100
print("Modified List:", my_list)


# 

# 2.Take any example of list on your own and perform atleast 5 list operations on that

# In[2]:


#write your code here
# Creating a list
numbers = [10, 20, 30, 40, 50]

# 1. Append an element
numbers.append(60)

# 2. Insert an element at index 2
numbers.insert(2, 25)

# 3. Remove an element
numbers.remove(40)

# 4. Reverse the list
numbers.reverse()

# 5. Sort the list
numbers.sort()

print("Final List:", numbers)



# 3.Create a new list containing only the even numbers from the original list.
# 
# original list ;[1,2,2,4,5,6,7,12,3,456,78,67,89,90]

# In[3]:


#write your code here
original_list = [1,2,2,4,5,6,7,12,3,456,78,67,89,90]
even_numbers = [num for num in original_list if num % 2 == 0]
print("Even Numbers:", even_numbers)


# 4.Create a new list with the squares of each element in the original list.
# 
# original list : [3,5,6,8,2,45]

# In[4]:


#write your code here
original_list = [3,5,6,8,2,45]
squared_list = [num**2 for num in original_list]
print(squared_list)


# 5.Check if all elements in the list are positive and return all the positive elements in a new list.
# 
# input ; [12,23,4,56,77,-89,7,90,90,-87,-99]

# In[5]:


# write your code here
input_list = [12,23,4,56,77,-89,7,90,90,-87,-99]
positive_list = [num for num in input_list if num > 0]
print("Positive Numbers:", positive_list)


# In[ ]:




