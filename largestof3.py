# Write a python program to find largest of three numbers. 
a=int(input("enter a="))
b=int(input("enter b="))
c=int(input("enter c="))

largest=0
if (a>b) and (a>c):
    largest=a
elif (b>c) and (b>a):
    largest=b
else:
    largest=c    

print("largest of ",a,b,"and",c,"=",largest)    