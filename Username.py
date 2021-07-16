#!/usr/bin/env python
# coding: utf-8

# Codeland Username Validation
# 
# Codeland Username Validation
# Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username according to the following rules:
# 
# 1. The username is between 4 and 25 characters.
# 2. It must start with a letter.
# 3. It can only contain letters, numbers, and the underscore character.
# 4. It cannot end with an underscore character.
# 
# If the username is valid then your program should return the string true, otherwise return the string false.
# 
# note: the 'true' and 'false' returns is because codebyte would only accept those returns as correct, insted of python's boolean operators True and False 

# In[58]:


def CodelandUsernameValidation(strParam):
  lengthPass = False
  letterPass = False
  typePass = True
  underscorePass = False
  if len(strParam) >= 3 and len(strParam) < 26:
        lengthPass = True
  else: print('length fail')
 
  if strParam[0].isalpha():
        letterPass = True
  else: print('letter fail')
    
  for char in strParam:
    if char.isalpha() != True and char.isdigit() != True and char != '_':
        print('Type fail')
        typePass = False
        
  if strParam[len(strParam) - 1] != '_':
    underscorePass = True
  else:
    print('underscore fail')

  if lengthPass and letterPass and typePass and underscorePass:
    return 'true'
  else: 
    return 'false'

# keep this function call here 
print(CodelandUsernameValidation(input()))

