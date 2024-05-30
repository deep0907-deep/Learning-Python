# start from 0 by default and icrease by +1 
 
# range(start?, stop, stepsize (increase numbeer)?)

for i in range(2,10,2):
    print(i) # 2,4,6,8

for i in range(7): 
    print(i) # 0 to 6

for i in range(1,5):
    print(i) # not print 0 and 5 
    
for i in range(1,100,2):
    print(i) # 1 to 99 odd number
    
# print 1 to 100 even no.

for i in range(2,101,2):
    print(i) # 2 to 100 even number
    
#print multiplication table of a number n.

n = int(input("enter your no.:"))
for i in range(1,11): # (1,11) means 1 to 10 multiply by "n"
    print(n*i)
    
    
    