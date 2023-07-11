#working with dictionaries

student_scores = {
    "Harry": 81,
    "Ron": 85,
    "Draco": 94,
    "Hermione": 99,
}

#create empty dict
student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        #add new entry
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
