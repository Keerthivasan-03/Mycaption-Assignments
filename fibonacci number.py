x=int(input("Enter the number: "))
a=0
b=1
print(a)
if x>=0:
    for i in range(0,x):
        c=a+b
        a=b
        b=c
        print(c)
else:
    print("Enter the valid number")

