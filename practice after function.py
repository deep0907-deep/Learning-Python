#WAP to print len of list.(list is  parameter)
cities = ["vadodara", "surat" , "indor"]
movies = ["bahubali1", "bahubali2"]
def find_len(list):
    print(len(list))
    

find_len(cities)
find_len(movies)

#waf to print the element of a list in a single line.

cities = ["vadodara", "surat" , "indor"]
movies = ["bahubali1", "bahubali2"]

def find_len(list):
    for element in list:
        print(element, end=" ") # use end=" " for one line
 
find_len(cities)
print() # REMOVE % FROM THE O/P

# waf to factorial of n.
"""n = 4
factorial = 1
for i in range(1, n+1):
    factorial *= i
print(factorial)  
 # above logic run in function  like;"""

n = 4

def cal_fact(n):
    fact = 1
    
    for i in range(n, 0, -1):
        fact *= i
        
    print(fact)
    
cal_fact(4)
   
#waf to convert USD to INR.

def converter(usd_val):
    inr_val = usd_val*83
    print(usd_val, "USD =", inr_val, "INR")
    
converter(10)
    
    
    