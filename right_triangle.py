#  (a^2 + b^2) == c^2

a = int(input("Length of side 1:"))
b = int(input("Length of side 2:"))
c = int(input("Length of side 3:"))
#Determines if it's a right triangle
if (a**2 + b**2) == c**2:
    print("It's a right triangle")
else:
    print("It's not a right triangle")