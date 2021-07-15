#!/usr/bin/env python
# coding: utf-8

# Testing basic functionality, data types, functions, deccision statments and loops

# In[33]:


A = 1
B = 'hehe'
C = [1,2,"3"]


# In[12]:


print(A)
type(C)


# In[13]:


def subtractor(A, B):
    sum = A - B
    return sum
    


# In[15]:


subtractor(19, 5)


# In[31]:


i = 0
while len(C)>i:
    print(i)
    if i == 1:
        print('i is greater than 1')
    elif i > 2:
        print('hot danm')
    i = i+1
   


# In[46]:


type(C)

del C[1]


# In[36]:


dictionaryyy = {
    'hehe' : 3,
    'nana' : 'test',
    'andthird' : '22'
}


# Array Challenge
# 
# Have the function ArrayChallenge(arr) take the array of numbers stored in arr which will contain integers that represent the amount in dollars that a single stock is worth, and return the maximum profit that could have been made by buying stock on day x and selling stock on day y where y > x. For example: if arr is [44, 30, 24, 32, 35, 30, 40, 38, 15] then your program should return 16 because at index 2 the stock was worth $24 and at index 6 the stock was then worth $40, so if you bought the stock at 24 and sold it at 40, you would have made a profit of $16, which is the maximum profit that could have been made with this list of stock prices.
# 
# If there is not profit that could have been made with the stock prices, then your program should return -1. For example: arr is [10, 9, 8, 2] then your program should return -1.
# 
# note: Whilst this might not be the most appropriate solution, all steps were thought out without the help of any resources, including git or stackoverflow
# 
# Working solution bellow:

# In[26]:


arr = [11,2,3,4,5,6]
def ArrayChallenge(arr):
    biggestDif = 0
    i = 0
    j = 0 
    while i < len(arr):
        print('1st loop ith', arr[i])
        print(arr[i])
        j = i
        while j < len(arr):
            print('second',arr[j])
            Dif = arr[j] - arr[i]
            j = j+1
            print('differance is: ', Dif)
            if biggestDif < Dif:
                    biggestDif = Dif
                    print('change', biggestDif)
        i = i+1  
    return(biggestDif)
ArrayChallenge(arr)
            


# for loop solution attempted

# In[ ]:


arrr = [11,2,3,4,5,6]
def ArrayChallenge(arr):
    biggestDif = 0;
    for idx, i in enumerate(arr):
        print('1st loop ith', idx)
        indxx = idx
        for idxx,j in enumerate(arr):
                print(idxx)
                Dif = j - i
                print('diff' , Dif) 
                if biggestDif < Dif:
                    biggestDif = Dif
                    print(biggestDif)
                        
                    
            
        
    return biggestDif
            
    

# keep this function call here 
ArrayChallenge(arrr)


# In[ ]:




