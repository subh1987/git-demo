def avg_marks(marks):
    subject = len(marks)
    average_marks = sum(marks) / subject
    return average_marks

# Calculate the grade then return it
def calculate_grade(average_marks):
    if average_marks >=80:
        grade = 'A'
    elif average_marks >=60:
        grade = 'B'
    elif average_marks >=50:
        grade = 'C'
    else:
        grade = 'F'
    return grade
marks = [20,30,40,50,60]
average_marks = avg_marks(marks)
print("Your average marks is: ", average_marks)
grade = calculate_grade(average_marks)
print("Your grade is: ", grade)