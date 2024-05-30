"""for el in range(5):
    pass
print("some useful work")

# its only use of "pass statement" as a placeholder for fututre code

# practice que 
# 1. WAP to find sum of first n numbers.(using while)

n = int(input("enter your no.:"))
sum = 0
for i in range(1, n+1):
    sum += i   
print("total sum =", sum)


# 2. WAP to find factorial of first n numbers.(using for)
n = int(input("enter your no.:"))
factorial = 1
for i in range(n,0,-1):
    factorial *= i
print(factorial) """

#in while loop
n = int(input("enter your no.:"))
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1 
print(factorial) 

