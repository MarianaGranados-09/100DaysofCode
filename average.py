#calculating the average age
student_ages = input("Enter a list of student ages: ").split()
total = 0
avr = 0
for i in range(0, len(student_ages)):
    total += int(student_ages[i])

#print(total)
#print(student_ages)
avr = total / len(student_ages)
print(f"The average age is: {avr}")
