# String Methods -- count,find,rfind and string case methods


# we will use str1 as variable
# to count characters or substrings in the given string.
# The string method count helps to achieve this:
# count()

# syntax: str1.count[, start[, end]])

# The count method returns the number of occurrences of the substring substr in string
# str1. By using the parameter start and end you can obtain a slice of str1.

# example :
str1 = "THe Avengers"
print(str1.count("e"))

#3

print(str1.count("e",5,12))

# In may situations, we need to find the index of substring in the string.
# The find() method can do the task.

# Syntax : str.find(str, beg=0 end=len(string))
# Example :
str1 = "peace begins with a smile"
print(str1.find("with"))

# another example
str1 = "what we think, we become"
str2 = str1.find("we")
print(str2) #-->5

# In the preceding example, the "we" substring occurs two times, but the find method will
# only give the index of the first occurrence. If you want to find the occurrence from right,
# you can use the rfind method. Let's learn by example:

print(str1.rfind("we")) #-->15

# String Cases methods

# lower() method : the lower method returns a string in which all case-based characters are present in lower case.
# example :
name = "HaCkeR GAni"
print(name.lower())  # --> hacker gani

# upper() method : makes the charectors all uppercase
# Example :
print(name.upper()) #--> HACKER GANI

# capitalize() method : makes the first charector uppercase
# example :
print(name.lower().capitalize()) #--> Hacker gani

# title() method : making first charactor of every word
# example :
print(name.lower().title()) #--> Hacrker Gani

modi = "beta acchase coding seekle varna chai dookhan kolle"
print(modi.title())

# swapcase() method : this method allows the user to swap the cases
# Example :
print(modi.title()) #--> Beta Acchase Coding Seekle Varna Chai Dookhan Kolle
print(modi.title().swapcase()) #-->  bETA aCCHASE cODING sEEKLE vARNA cHAI dOOKHAN kOLLE
.
