'''
store following word meaning in python dictionary:
table: "a piece of furniture", "list of facts & figures"
cat : "a small animal
"'''
dictionary = {
  "table": ["a piece of furniture", "list of facts & figures"],
  "cat" : "a small animal"
 }
print(dictionary)


'''
you are given list of sub for students. 
Assume one classroom is req for 1 sub.
How many classrooms are needed by all students

"python","java", "c++", "python", "javascript",
"java", "python", "java", "c++", "C"

'''
sub = {
    "python","java", "c++", "python", "javascript","java", "python", "java", "c++", "c"
}
print(len(sub))

"""
wap to enter marks of 3 sub from user and store them in a dictionary.
start with empty dictionary & add one by one.
use sub name as key & marks as value.  

"""
marks = {}
a = int(input("enter python marks:"))
b = int(input("enter c++ marks:"))
c = int(input("enter php marks:"))

marks.update({"python" : a})
marks.update({"c++" : b})
marks.update({"php" : c})

print(marks)

"""Figure out way to store 9 & 9.0 as seprate values in set
"""
#method :1 
values = {9,9.0}
values1 = {9,"9.0"}
print(values1)
print(values)

#method :2
values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)