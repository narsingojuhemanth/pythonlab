#*
#* *
#* * *
#* * * *
#* * * * *
#* * * *
#* * *
#* *
#*

n=int(input("enter max stars in row"))

for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print(end="\n")

for i in range(n-1,0,-1):
    for j in range(i):
        print("*",end=" ")
    print(end="\n")


