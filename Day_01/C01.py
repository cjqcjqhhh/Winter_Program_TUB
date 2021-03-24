#!/usr/bin/env python
# coding: utf-8

# # Test

# In[ ]:


from urllib.request import urlopen

html = urlopen(
    "https://morvanzhou.github.io/static/scraping/basic-structure.html"
).read().decode('utf-8')

import re

res = re.findall(r"<title>(.+?)</title>", html)
print("\nPage title is: ", res[0])


# In[2]:


print("hello world")


# # Variables

# In[11]:


x = 5
print(type(x))
x = x+ 0.1
print(type(x))
x = True
print(type(x))


# In[14]:


b = (1,2,3)
print(type(b))
b = [1,2,3]
print(type(b))


# # Operation

# In[16]:


#square root
4**0.5


# In[21]:


list1 = [1,2,3,4]
list2 = [2,3,4]
list1 + list2


# In[22]:


#but we can't minor two list
list1 - list2


# ## Difference between Tuple and list

# In[24]:


#tuple 
t = (1,2,3)
print(type(t))
l = [1,2,3,4]
print(type(l))


# In[ ]:


#tuple cna not be changed


# # Bool

# In[25]:


True or False


# In[26]:


False is False


# In[28]:


a = 1
b = 1
a is b
# is can be used to check two variables


# In[31]:


t = (1,2,3)
l = (1,2,3)
t is l
# if check is two variables is the same


# In[32]:


t == l
# but the '==' check the value


# In[35]:


(1,2,3) is (1,2,3)


# In[36]:


[1,2,3] is [1,2,3]


# # if else

# In[37]:


if True:
    print("hahahahahaha")
# check is boolean operation return


# In[39]:


if False or False and True or True:
    print("really?")
# and always has higher priority than or???
# I cannot find a right way to check it


# # String

# In[42]:


# you can simplely add up to string by +
str1 = "hello "
str2 = "Im junqi"
str1 + str2


# In[46]:


str3 = str1*3
str3


# ## some useful function for string

# In[48]:


#I wonder how does this function list used for
list()
#???


# In[49]:


len(str1)


# In[69]:


l1 = [1,2,3,4,5]
l1.append(6)
print(l1)


# In[70]:


len(l1)


# In[71]:


#Attention: if you run a block multiple times it will execute multiple times


# In[72]:


l1.append("another type")
l1
#cuz I exe 3 times here


# In[73]:


# get the value of list: use the index
l1[0]


# In[74]:


l1.remove(2)
l1


# In[75]:


x = l1.pop(3)
x, l1
# 3 is the 4th number of the list


# # list indexing and sclicing

# In[76]:


# remember list is contained in []
list1 = [1,2,3]
list1[0:2]
# only give the index from 0 to 1
# cuz the for is end before the last number 2


# In[82]:


#begin from the first index and end before the last index
list1[-2:-1]


# In[83]:


list1[-2:]


# In[84]:


list1[-1:-3]
# the first index should be lower than the end index or it will give the blank list


# In[85]:


list2 = [1,3,1,2,1,4,1]
list2[1:7:2]


# In[86]:


list2[-1:-5:-1]


# In[87]:


list2[::2]


# In[89]:


#intereting one!!!
list3 = [0,1,2,3,4,5,6,7,8]
list3[7:-9:-3]


# In[ ]:




