student={
    "name" : "deep",
    "sub" : {
        "phy" : 82,
        "chem": 71,
        "maths":80
    }
}

print(student)
print(student.keys())
print(list(student.keys()))
print(len(list(student.keys())))

#print(student["name2"]) -------- ERROR
print(student.get("name2")) #NO ERROR

