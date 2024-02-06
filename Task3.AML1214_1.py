#!/usr/bin/env python
# coding: utf-8

# In[139]:


import pandas as pd


# In[140]:


#3.4
# Defining my guests
guests = ["Alice", "Michael", "Luccas"]

#Create the invite for all
def create_invitation() :    
    for guest in guests :
        print (f"Dear {guest}, \n\nYou are invited to an Brazilian dinner at my place on this Saturday at 7pm.\n\nSee you there\nAldo ")
        print ("\n")

#Printing the invitations
create_invitation()


# In[141]:


#3.5
#Printing the guest list with out changing
print (guests)
#Removing the guest that can´t go to the dinner
guests.pop(1)
#Printing the new guest list
print (guests)

#Printing the invitations
create_invitation()


# In[142]:


#3.6
#The guests lists without change
print(guests)
#Adding the guest in the begging of the list
guests.insert(0, "Marcelo")
#Adding the guest in the middle of the list
guests.insert(2, "Fernanda")
#Adding the guest in the end of the list
guests.append("Karoline")
#The guests lists after change
print(guests)

#Printing the invitations
create_invitation()


# In[143]:


#3.7
#Printing the guest list without changing
print(guests)
#Creating am Sorry message to all the guests
  
for guest in guests :
    print (f"Dear {guest},\n\nUnfortunetally I discovery my table will not arrive at time, so Let´s make it another time with every one, at this moment i can just recive 2 guests\nSorry\nAldo ")
    print ("\n")
#Poping the persons for the guest list
print (f"Dear {guests[0]},\n\nUnfortunetally, after some random choices you got selected to be in the next time dinner\nSorry\nAldo ")
guests.pop(0)
print (f"Dear {guests[2]},\n\nUnfortunetally, after some random choices you got selected to be in the next time dinner\nSorry\nAldo ")
guests.pop(2)
print (f"Dear {guests[2]},\n\nUnfortunetally, after some random choices you got selected to be in the next time dinner\nSorry\nAldo ")
guests.pop(2)
#Printing the guest list after poping
print(guests)
#Printing the invitations the the two left
create_invitation()
last_guys_standing = guests.copy()
#Deleting my guest list
del guests[:]
#Printing the guest list
print(guests)


# In[144]:


#3.8
#Saving the list of the citys that I want to go
citys = ["Switzerland", "Japan", "Amsterdam", "Greece", "Mexico"]
#Printing the citys
print(citys)
#sorted function
alpha = sorted(citys)
#Printing the in alphabetical order the citys
print("\n")
print(alpha)
#reverse function
rev = alpha
rev.reverse()
#Printing in the reverse order
print("\n")
print(rev)
#Sort function
alpha.sort()
#printin in the sort function
print("\n")
print (alpha)
#Sort function
rev.sort()
#printin in the sort function
print("\n")
print (rev)


# In[147]:


#3.9
#Using Len
len_guests = len(last_guys_standing)
#Printing the number of guests invited
print(len_guests)


# In[149]:


#3.10
#Creating the list
listy = ["Rivers", "Montains", "Forests"]
#Printing
print(listy)
#Addinging new stuff
listy.insert(0, "Citys")
#Adding new stuff in the end
listy.append("Languages")
#Printing
print(listy)
#Pop
listy.pop(0)
#Priting
print(listy)
#Stored
alpha = sorted(listy)
#Printing the in alphabetical order the citys
print("\n")
print(alpha)
#reverse function
rev = alpha
rev.reverse()
#Printing in the reverse order
print("\n")
print(rev)
#Sort function
rev.sort()
#printin in the sort function
print("\n")
print (rev)
#Last list
last_listy_standing = listy.copy()
#Deleting my guest list
del listy[:]
#Printing the guest list
print(listy)


# In[ ]:




