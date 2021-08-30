#!/usr/bin/env python
# coding: utf-8

# In[57]:


# Import Libraries 

import random
import string 


# In[80]:


def generate_password(username):
    """
    A function to generate a password from a username
    
    Params: String: username
    Returns: String: Random Strong Password
    
    Sample Input: ibrahim
    Sample Output: 20138IbrahiM!\"&=
    
    """
    # Convert the first and last character to uppercase
    password = username[0].upper() + username[1:-1].lower() + username[-1].upper()
    
    # Store number and symbols form string library
    num = string.digits
    symbols = string.punctuation
    
    # Generate random symbols and numbers with the length of 5
    strtemp1 = "".join(random.sample(num,5))
    strtemp2 = "".join(random.sample(symbols,5))

    
    # Concatenate username with the generated symbols and numbers
    p = strtemp1 + password + strtemp2
    
    #Return the generated password
    return p


# In[81]:


# Take the username from user
username = str(input('\n Enter your user name to generate a password: '))

#Print the generated password
print("Your Password Is: " + generate_password(username))

