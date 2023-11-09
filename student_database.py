student_database=[

                {"Name":"Tamil varma",
                 "Reg No":4698746,
                  "dept":"Mechanical",
                  "sub1" : 80,
                   "sub2" : 88,
                   "sub3" :90

                   },
                  {
                    "Name":"Kaviya",
                      "Reg No":35674,
                      "dept":"CSE",
                      "sub1" : 89,
                      "sub2" : 97,
                      "sub3" : 78
                  },
                  {
                      "Name":"Sivaraj",
                      "Reg No": 66276,
                      "dept":"mechanical",
                      "sub1" : 77,
                      "sub2" : 88,
                      "sub3" : 76

                  }]

for x in student_database:
    print("student name is",x["Name"],"and reg no is",x["Reg No"],"he is persuing",x["dept"],"Department")


for x in student_database:
    print("student name:",x["Name"])

for x in student_database:
    if x["dept"] == "CSE":
        print("Student name:",x["Name"])


for x in student_database:
    Y = (x["sub1"]+x["sub2"]+x["sub3"])/3

    print(Y)

    if Y > 90:
        Value = "A"
    elif  Y > 80:
        Value = 'B'
    elif Y > 70:
        Value = 'C'
    else:
        Value = 'D'
    x["GRADE"] = Value



    x["CGPA"] = Y
    
print(student_database)

first_rank_name = " "
first_rank = 0
for x in student_database:
    if x["CGPA"] > first_rank:
        first_rank = x["CGPA"]
        first_rank_name = x["Name"]

print(first_rank_name)


