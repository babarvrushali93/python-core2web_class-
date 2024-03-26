#!/usr/bin/env python
# coding: utf-8

# 1. WAP to check numbers are divisible by 4 and 5 print those numbers
# input1 : num1=20
# output:20 is divisible by 4 and 5
# input1 : num1=15
# output:15 is not divisible by 4 and 5       

# In[4]:


num1 = int(input("Enter the num1: "))

if(num1 % 4 == 0)and(num1 % 5 == 0):
    print("%d is divisible by 4 and 5" %num1)
else:
    print("%d is not divisible by 4 and 5" %num1)


# 2. WAP to determine entered angles define a right-angled triangle.take three values of angle form the user.
# input1:angel1 = 90
# input2:angel2 = 90
# input3:angel3 = 90
# output: It is not a right-angle triangle
#     
# input1:angel1 = 90
# input2:angel2 = 60
# input3:angel3 = 30
# output: It is a right-angle triangle    

# In[3]:


angel1 = int(input("Enter the values of angel1: "))
angel2 = int(input("Enter the values of angel2: "))
angel3 = int(input("Enter the values of angel3: "))


if(angel1+angel2+angel3 == 180):
    print("It is a right-angle triangle")
else:
    print("It is not a right-angle triangle")


# 3. Take two numbers from users and print the sum of those numbers if the sum is even.
# 
# input1 :num1 = 20
# input2 :num2 = 20   
# output: 40 is Even 
#     
# input1 :num1 = 10
# input2 :num2 = 25  
# output:No Output   
#     

# In[19]:


num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))

sum = num1 + num2

if(sum % 2 == 0):
    print(sum,"is even")
else:
    print("No Output")


# 4. Take a number from the user and check whether it is present in the list.if it's in the list print "Available."
# 
# list1 = [10,20,30,40,50]
# 
# input :num:10
# output: available
#     
# input :num:15
# output: No output
#         

# In[33]:


num = int(input("Enter the num: "))

list1 = [10,20,30,40,50]

if num in list1:
    print("Available")
else:
    print("no Output")
    


#  5. print the "core2web" string a number a times entered by the user if the
#     number is even.
#     
#     input: num = 2
#     output:core2web
#            core2web
#      
#     input: num = 5
#     output:No Output      

# In[37]:


num = int(input("Enter the number: "))

if(num % 2 == 0) :
    print(num * "Core2web")
else:
    print("No Output")


# 6. write a program that checks if a given number is odd using thr "if" statements.
# 
#     input: num = 13
#     output:odd
#     
#    input :num = 12
#    output:No Output    

# In[43]:


num = int(input("Enter the number:"))

if(num % 2 != 0):
    print("%d is Odd number" %num)
else:
    print(" No output" )


# 7. take two numbers form the user ,check if both are odd and then print the sum of the numbers.
# 
# input : num1 = 10
# input : num2 = 11
# output : 21
#     
# input : num1 = 10
# input : num2 = 6
# output : No Output  

# In[16]:


num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))


if(num1 % 2 != 0) and (num2 % 2 != 0):
    print("both number are odd")
    print("sum of",num1 ,"and ",num2 , "is:", num1 +num2)
else:
    print("No Output")


# 8. take single character from user check if the ascii value of character is Even the print character.
# 
#     input: char1 = 'B'
#     output : B
#  
#     input: char1 = 'C'
#     output : No Output
#     

# In[2]:


char1 = input("Enter the single char1: ")
      
if (len(char1) == 1):
    ascii_value = ord(char1)
    if (ascii_value % 2 == 0):
          print("The ASCII value of", char1, "is even:", ascii_value)
    else:
        print("No Output")
else:
    print("Please enter only a single character.")


# 9. Take Two character from user check if the ascii value both of character are odd then print the sum of ascii values of character.
# 
#     input: char1 = 'A'
#            char2 = 'C'
#     output: 132
#     
# 
#     input: char1 = 'a'
#            char2 = 'b'
#     output: No Output
#         

# In[16]:


char1 = input("Enter the char1: ")
char2 = input("Enter the char2: ")

ascii_value1 = ord(char1)
ascii_value2 = ord(char2)

if(len(char1) == 1)&(len(char2) == 1):
    if (ascii_value1 % 2 != 0) and (ascii_value2 % 2 != 0):
         print("The ASCII value of sum  is Odd:",(ascii_value1+ascii_value2))
    else:
        print("No Output")


# 10. Take the number from user and  modulus with 8 if the reminder of the number is 3 then print reminder.
# 
# input: num = 27
# output: 3
#     
# 
# input: num = 10
# output: No Output
#         

# In[28]:


num = int(input("Enter the num: "))


if(num % 8 == 3):
    print("Remainder is:", num % 8 )
else:
     print("No Output")


# In[ ]:




