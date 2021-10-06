#!/usr/bin/env python
# coding: utf-8

# In[19]:


#creating heights list 
heights = [61, 70, 67, 64]


# In[20]:


#creating names list
names = ["Noelle", "Ava", "Sam", "Mia"]


# In[21]:


#creating mixed list
mixed_list_common = ["Mia", 27, False, 0.5]


# In[22]:


append_example = [ 'This', 'is', 'an', 'example']
append_example.append('list')
 
print(append_example)


# In[23]:


garden = []

garden.append("Tomatoes")
 
print(garden)

# Create a list
garden = ["Tomatoes", "Grapes", "Cauliflower"]
 
# Append a new element
garden.append("Green Beans")
print(garden)


# In[24]:


#growing list
items_sold = ["cake", "cookie", "bread"]

#Suppose the bakery wants to start selling "biscuit" and "tart":


items_sold_new = items_sold + ["biscuit", "tart"]
print(items_sold_new)
# We can inspect the original items_sold and see that it did not change:


print(items_sold)
#We can only use + with other lists. If we type in this code:


my_list = [1, 2, 3]

#If we want to add a single element using +, we have to put it into a list with brackets ([]):

my_list + [4]


# In[25]:


#Accessing List Elements

calls = ["Juan", "Zofia", "Amare", "Ezio", "Ananya"]
print(calls[2])


# In[26]:


#Accessing List Elements: Negative Index

pancake_recipe = ["eggs", "flour", "butter", "milk", "sugar", "love"]

#If we select the -1 index, we get the final element, "love".


print(pancake_recipe[-1])


# In[27]:


#Modifying List Elements

garden = ["Tomatoes", "Green Beans", "Cauliflower", "Grapes"]

garden[2] = "Strawberries"
 
print(garden)

#Negative indices will work as well. 

garden[-1] = "Raspberries"
 
print(garden)


# In[28]:


#Shrinking a List: Remove
shopping_line = ["Cole", "Kip", "Chris", "Sylvana"]

#We could remove "Chris" by using the .remove() method:


shopping_line.remove("Chris")
 
print(shopping_line)

# Create a list
shopping_line = ["Cole", "Kip", "Chris", "Sylvana", "Chris"]
 
# Remove a element
shopping_line.remove("Chris")
print(shopping_line)


# In[34]:


#Two-Dimensional (2D) Lists

#We can put several of these lists into one list, such that each entry in the list represents a student and their height:


heights = [["Noelle", 61], ["Ava", 70], ["Sam", 67], ["Mia", 64]]

#We will often find that a two-dimensional list is a very good structure for representing grids such as games like tic-tac-toe. 


#A 2d list with three lists in each of the indices. 
tic_tac_toe = [
            [["X"],["O"],["X"]], 
            [["O"],["X"],["O"]], 
            [["O"],["O"],["X"]]
]

#Accessing 2D Lists


#Let’s return to our classroom heights example:


heights = [["Noelle", 61], ["Ali", 70], ["Sam", 67]]

#Access the sublist at index 0, and then access the 1st index of that sublist. 
Noelles_height = heights[0][1] 
print(Noelles_height)


# In[35]:


#Modifying 2D Lists

class_name_hobbies = [["Jenny", "Breakdancing"], ["Alexus", "Photography"], ["Grace", "Soccer"]]

class_name_hobbies[0][1] = "Meditation"
print(class_name_hobbies)


# In[ ]:




