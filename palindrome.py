#wap to check if list contain a palindrome of elements (hint: copy())
   # [1,2,3,2,1] [1,"abc","abc",1]

list1 = [1,2,1]
copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("Not palindrome")