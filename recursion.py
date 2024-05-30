def show(n):  
    if( n==0): #base case jb n=0 aajaye tab process rok do
        return
    print(n)
    show(n-1) #print in loop n==5 and 5-1=4
    
show(5) #5,4,3,2,1(n,n-1,n-2,n-3,n-4)

