#WAP TO CHECK IF A NUMBER ENTERED BY THE USER IS ODD OR EVEN

a = int(input("enter your number: "))

rem = a % 2

if (rem == 0):
    print("EVEN")
else:
    print("ODD")
