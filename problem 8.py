#wap to find the gratest of 3 no. entered by user

a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if(a >= b and a >= c):
    print("first number is largest", a)
elif(b >= c):
    print("second numer is largest", b)
else:
    print("third is largest", c)

