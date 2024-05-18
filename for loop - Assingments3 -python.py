#!/usr/bin/env python
# coding: utf-8

# # python Assignment-3
# # Topics - for loop

# # 1. write a program to print the first 10 numbers.

# In[3]:


for i in range(1,11):
    print(i)


# # 2. write a program to print the first 100 numbers

# In[4]:


for i in range(1,101):
    print(i)


# # 3. write a program to print the first ten ,3 digit number.

# In[5]:


for i in range(100,110):
    print(i)


# # 4.write a program to print even numbers 1-100.

# In[9]:


for i in range(1,101):
    if i % 2 ==0:
        print(i)


# # 4.write a program to print odd numbers 1-50.

# In[14]:


for i in range(1,51):
    if i % 2 == 1:
        print(i)


# In[ ]:


6. write a program to reverse from 100-1.


# In[26]:


for i in range(100,0,-1):
       print(i)


# # 7. write a program to print a table 12.

# In[14]:


for i in range(1,11):
    print(i*12)


# # 8. write a program to  print a table of 12 in reverse order.

# In[23]:


for i in range(10,0,-1):
    print(i*12)


# # 9. write a program to print the sum of the first 10 numbers.

# In[44]:


total_sum = 0
for i in range(1,11):
    total_sum += i
print("The sum of the first 10 numbers is:",total_sum)


# # 10. write a program to print the product of the first 10 numbers.

# In[53]:


product = 1
for i in range(1,11):
    product *= i
print("The product of the first 10 numbers is:",product)


# In[ ]:




