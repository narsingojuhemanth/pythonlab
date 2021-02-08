lower=int(input("enter lower limit="))
upper=int(input("enter upper limit="))

for num in range(lower,upper+1):
    if num >0:
        for j in range(2,num):
            if num%j==0:
                break
        else:
            print(num)
