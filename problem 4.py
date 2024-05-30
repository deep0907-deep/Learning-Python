#GRADE STUDENTS BASED ON MARKS

marks = int(input("ENTER YOUR MARKS: "))

if(marks >= 90):
    grade = "A"

elif(marks >=80 and marks <90):
    grade = "B"

elif(marks >= 70 and marks <80 ):
    grade = "C"

else: 
    grade = "D"

print("grade of student :", grade)
