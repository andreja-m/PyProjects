def calculateGPA(gradeDict):
    return sum(gradeDict.values())/len(gradeDict)

students = {}
# We can set the keys to variables so we might minimize typos
name, age, gender, level, grades = "name", "age", "gender", "level", "grades"
john, jane = "john", "jane"
math = "math"
students[john] = {}
students[john][age] = 12
students[john][gender] = "male"
students[john][level] = 6
students[john][grades] = {math:3.3}

students[jane] = {}
students[jane][age] = 12
students[jane][gender] = "female"
students[jane][level] = 6
students[jane][grades] = {math:3.5}

# At this point, we need to remember who the students are and where the grades are stored. Not a huge deal, but avoided by OOP.
print(calculateGPA(students[john][grades]))
print(calculateGPA(students[jane][grades]))

