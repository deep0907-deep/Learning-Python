"""
 Two types of LOOPS:
 1.while
 2.for 

"""
'''count = 1
while count <=5:
    print("hello")
    count += 1 #use of check increasing value and when condition is false then its stop
    '''
#print no from 1 to 10
'''i = 10
while i >= 1:   
    print(i)
    i -= 1'''

#practice example

#PRINT NUMBER FROM 1 TO 1000

"""
i = 1 
while i<= 100:
    print(i) 
    i +=1
"""
# PRINT MULTIPLICATION TABLE OF NUBNER n.
"""
i=1
n = int(input("enter your number:"))
while i<=10:
    print(n*i)
    i+=1
"""
#print element of the following list using a loop:
 # [1,4,9,16,25,36,49,64,81,100] 

"""nums=[1,4,9,16,25,36,49,64,81,100] 

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1
"""
#find 36 from above list
nums=[1,4,9,16,25,36,49,64,81,100] 
x=36
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at index",i) 
    else:
        print("finding..")
    i += 1 

