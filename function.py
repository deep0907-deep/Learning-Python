#  function use for "reduce number of CodeLine"

# so, def ---> define for function 
"""
def fun_name( param1, param2...):

   #sum_work
   
   return val
   
func_name( arg1, arg2...) #function call

"""

"""def cal_sum(a, b):
    sum = a+b 
    print(sum)
    return sum 
cal_sum(2, 10)
cal_sum(5, 12)
cal_sum(4, 9)"""

#redundation 

"""
a = 5
b = 10

sum = a + b
print(sum)"""   

#function defination
def calc_sum(a, b): #parameter
    return a + b 

sum = calc_sum(178, 22) #function call; arguments
print(sum)


# also return as a default parameter using
def calc_sum(a=5, b=4): #parameter
    print(a + b)
    return a + b 

calc_sum() #function call; arguments


#avg of 3 number 

def cal_avg(a, b, c):
    sum = a+b+c
    avg = sum / 3
    print(avg)
    return avg

cal_avg(1,2,3)
    