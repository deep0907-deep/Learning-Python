#conditional statement 

a  = int(input("ENTER YOUR AGE: "))

if(a >= 18):
    print("can vote & apply for licence")

elif(a < 18):
    print("can not vote & apply for licence")

else:
    print("can not") 

""" if or elif me kya difference h ?
if ki condition jab false hoti h tb elif work krta h 

else me koi condition nai hoti h 
if elif sari uppar ki condition false hojaye tb direct else statement 
                                                       print ho jata h
"""