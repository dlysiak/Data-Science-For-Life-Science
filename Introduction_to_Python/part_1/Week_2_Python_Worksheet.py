#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 09:52:46 2020

@author: stephen
"""

# =============================================================================
# [1] Carry out basic mathematic operations using python
# =============================================================================
#%%
# [i]    addition
2+4
#%%
# [ii]  subtraction
4-7
#%%
# [iii] multiplication
6*5
#%%
# [iv]  division
6/3
#%%
# [v]   exponent
7**7
#%%
#%%

# =============================================================================
# [2] Assign and update a variable
# =============================================================================
#%%
# [i]    Assign a value to a variable
my_var = 6
#%%
# [ii]   Print that variable 
print(my_var)

#%%
# [iii]  Update that variable to make it a new value
my_var = my_var*2 
#%%
# [iv]   Print the variable to see if it updated
print(my_var)

#%%

# =============================================================================
# [3] Working with strings
# =============================================================================

# [i]   Assign your name, in string format, to an aptly named variable
#%%
name = "Daria"
# [ii]  Check to see that the value in your variable is a string
#%%
type(name)

# [iii] Change all of the characters in the variable to lower case
#%%
name.lower()
# [iv]  Use f strings to create a message which includes your name variable
#%%
print(f"My name is " + name)
# [v]   Create a string of ten numbers separated by commas
numbers = "2,3,4,5,6,7,8,9,10,1"

#%%
# =============================================================================
#  [4] Working with lists
# =============================================================================

# [i]   Take the string you created in [3][v] and turn it into a list
#%%
numbers_list = numbers.split(",")
print(numbers_list)
# [ii]  Get the value of the third item in the list
#%%
numbers_list[2]
# [iii] Get the same value but use negative indexing
#%%
numbers_list[-8]
# [iv]  Get the first two items in the list using slice notation
#%%
numbers_list[0:2]
# [v]   Get every second item from the list
#%%
numbers_list[::2]
# [vi]  Update item at index 5 to a new value
#%%
numbers_list[4] = 8
# [vii] Update item at index 6 to a new value which is the sum of
#       the value of item index 2 and item index 3 together
#%%
numbers_list[5] = int(numbers_list[1]) + int(numbers_list[2])
# [viii] Add a new value to the end of the list
#%%
numbers_list.append(13)
print(numbers_list)
# [ix]  Delete the value at item index 5
#%%
del numbers_list[4]
#%%

# =============================================================================
# [5] Working with dictionaries
# =============================================================================

# [i]   Create a dictionary with two keys, have the first key contain
#       a list of integers and the second key contain a list of strings

#%%
my_dict = {"first":[1,2,3], "second":["string1", "string2", "string3"]}
# [ii]  Print out only the second keys values
#%%
my_dict["second"]
# [iii] Get the value of the first item in the first keys values
#%%
my_dict["first"][0]
#%%
# =============================================================================
#  [6] Conditional statements
# =============================================================================

x = 100
y = 200

# [i]   Does x equal y
#%%
x == y 
# [ii]  Does either x or y equal 200
#%%
x == 200 or y == 200
# [iii] Does x and y equal 50
#%%
x ==50 and y== 50
# [iv]  Does half of y equal x?
#%%
0.5 * y == x
#[v]    Does half of y equal x and does double x equal y
#%%
0.5 *y == x and 2*x == y
#%%
# =============================================================================
#  [7]  For loops
# =============================================================================

# [i]   Create a for loop which loops over the list you created in [3][v]
#       and prints each item into a f string.
#%%
for fig in numbers.split(","):
    print(f"{fig} ia an element of the list of numbers")


#%%


# [ii]  Create a for loop which will only print the value of the item
#       in the list if it is greater than or equal to the last item in the list
#%%
for fig in numbers.split(","):
    if int(fig) >= int(numbers[-1]):
        print(fig)


#%%
# [iii] Create a for loop which will loop over your list and append each item to
#       a new list
#%%
new_list = []
for fig in numbers.split(","):
    new_list.append(int(fig))
print(new_list)
print(my_list)
#%%
# =============================================================================
#  [8] Create a function
# =============================================================================

# [i] Create a function which asks for the users details and returns a dictionary
#     with the keys 'Name', 'Date of birth', and 'Nationality'.
#     Assign the output to a variable.

#%%
def personal_details(name,dob,nationality):
    name = input("Enter your name: ") 
    dob = input("Enter your date of birth: ")
    nationality = input("Enter your nationality: ")
    return {'Name': name, "Date of birth": dob, "Nationality": nationality}

darias_details = personal_details()
