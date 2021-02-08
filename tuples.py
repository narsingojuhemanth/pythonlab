#Write a program to demonstrate working with tuples in python. 

#create
s=(1,2,3,"hello",12+3j)
print(s)
print(s[3])
print(s[3][2])

s=1,2,3
print(type(s))
print(s)

# s[1]=123 #'tuple' object does not support item assignment

my_tuple = () # Empty tuple
print(my_tuple)
my_tuple = (1, 2, 3) # Tuple having integers
print(my_tuple)
my_tuple = (1, "Hello", 3.4) # tuple with mixed datatypes
print(my_tuple)
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3)) # nested tuple
print(my_tuple)

my_tuple = ("hello")
print(type(my_tuple)) # <class 'str'>
# Creating a tuple having one element
my_tuple = ("hello",)
print(type(my_tuple)) # <class 'tuple'>
# Parentheses is optional
my_tuple = "hello",
print(type(my_tuple)) # <class 'tuple'>

#del
del my_tuple

