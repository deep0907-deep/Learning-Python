#read & write data on a file 
"""
two types of file i/o in python
1.TEXT FILE: .txt, .docx, .log
2.BINARY FILLE: .mp4, .png, .jpeg 

how can write in code
 f = open("file_name", "mode")

character                 Meaning
'r'      open for reading 
'w'      open for writing, truncating file first
'x'      create a new file and open it for writinh
'a'      open for writing, appending to the end of the first if it exists
'b'      binary mode
't'      text mode
'+'      open a disk file for updating(reading and writinng)

'r+'     read + overwrite (pointer starting)---------no truncte(file data not delete)
'w+'                                        ---------truncte
'a+'     read append(poiter starting)

"""
              # Read a file 
"""              
f = open("demo.txt", 'r+t')

#data = f.read(8) #only read 8 characters 

line1 = f.readline() # perticular koi line ko print karavane ke liye use krte h
print(line1) 

line2 = f.readline() # perticular koi line ko print karavane ke liye use krte h
print(line2) 

#print(data)
f.close()
"""


             # Write a file 
"""
f = open("demo.txt", 'a')

f.write("alert for holiday ") # use for above character to action write demp.txt file

f.close() # for more details visit stack overflow website"""




  # \\\ with Syntax \\\ --------- format of open file and close syntax
"""
with open("demo.txt", "r") as f: 
    data = f.read()
    print(data)"""
# with syntax was automatic  close file     

"""
with open("demo.txt", "w") as f:
    f.write("new data")
    
"""

                    # DELETING A FILE 

# import tensorflow---------> pip/pip3 install tanserflow
#using the os model

"""
import os

os.remove("sample.txt") # editor me file-red line ayegi plz open sample.txt

"""

# PRACTICE QUE 1\
    # CREAT THE NEW FILE "PRACTICE.TXT" USING PYTHON. ADD THE FOLLOWING DATA IN IT
"""  
Hi everyone 
we are learning file I/O
using Java 
I like programing in java

1.WAF that replace all occurances of "java" with "python" in above file.

2.Search if the world " learning" exits in the file or not.
"""
       #1.
with open("practice.txt","r") as f:
   data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open("practice.txt","w") as f:
   f.write(new_data)
   
       #2. 
def check_for_word():
    word = "learning"
    with open("practice.txt","r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("found")
        else:
            print("not found")
check_for_word()

# PRACTICE QUE 2\
    # WAF to find in which line of file docs the word"learning" occur first.
    # print-1 if word not found
    

   
        
def check_for_line():
    word = "learning"
    with open("practice.txt","r") as f:
        data = True
        line_no = 1
        with open("practice.txt", "r") as f:
            while data:
                data = f.readline()
                if(word in data):
                    print(line_no)
                    return
                line_no += 1
                
    return -1

print(check_for_line())

#Problem 3
# From a file contacting nubers seprated by comma, print the count of even numbers.

# for example 1,2,45,55,86,76
"""
step 1: individual number---------by split method
step 2: casting to int 
step 3: print even int
step 4.
    """
"""
with open("practice.txt", "r") as f:
    data = f.read()
    print(data) 
    
    num = ""
    for i in range(len(data)):
        if(data[i] == ","): 
            print(int(num))
            num = ""
        else:
            num += data[i]
"""


count = 0
with open("practice.txt", "r") as f:
    data = f.read()
    print(data) 
    
    # num = ""
    nums = data.split(",")
    print(nums)
    for val in nums:
        if(int(val) % 2 == 0): 
            count += 1
          
print(count)

# next ch.8 oops 7:55:25 