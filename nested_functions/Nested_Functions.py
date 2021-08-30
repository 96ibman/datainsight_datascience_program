#!/usr/bin/env python
# coding: utf-8

# # Nested Functions

# **Let's say that we want to use a process a number of times within a function** <br>
# For example, we want a function that takes 3 numbers as parameters <br>
# and performs the same function on each of them. <br>
# One way would be to write out the computation 3 times

# In[2]:


def mod2plus5(x1,x2,x3):
    """Returns the remainder plus 5 of three values."""
    new_x1 = x1 % 2 + 5 
    new_x2 = x2 % 2 + 5 
    new_x3 = x3 % 2 + 5 
    
    return(new_x1,new_x2,new_x3)
print(mod2plus5(1,2,3))


# **However, this definitely does not scale if you need to perform the computation many times** <br>
# What we can do instead is define an inner function within our function definition,<br>
# such as we will do next, and call it where necessary.<br>
# This is called a nested function. <br>
# The syntax for the inner function is exactly the same as that for any other function.

# In[3]:


def mod2plus5(x1,x2,x3):
    """Returns the remainder plus 5 of three values."""
    
    def inner(x):
        """Returns the remainder plus 5 of a value."""
        return x % 2 + 5
    
    return(inner(x1),inner(x2),inner(x3))
print(mod2plus5(1,2,3))


# # Return in Nested Functions

# In[4]:


def raise_val(n):
    """Return the inner function."""
    
    def inner(x):
        """Raise x to the power of n."""
        
        raised = x ** n
        return raised
    return inner


# - Let's now look at another important use case of nested functions. 
# - In this example, we define a function raise_vals, which contains an inner function called inner. 
# - Now look at what raise_vals returns: it returns the inner function inner! 
# - raise_vals takes an argument n and creates a function inner that returns the nth power of any number. 
# - That's a bit complicated and will be clearer when we use the function raise_vals. 

# In[5]:


square = raise_val(2)
cube = raise_val(3)
print(square(2), cube(4))


# - Passing the number 2 to raise_vals creates a function that squares any number. 
# - Similarly, passing the number 3 to raise_vals creates a function that cubes any number. 
# - One interesting detail: when we call the function square, it remembers the value n=2, although the enclosing scope defined by raise_val and to which n=2 is local, has finished execution. 
# - This is a subtlety referred to as a closure in Computer Science circles and shouldn't concern you too much.
# - That is why it is also called enclosing function 
