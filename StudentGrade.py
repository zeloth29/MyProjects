StuAge = int(input("Enter age of student\n>"))
if StuAge >= 10 and StuAge < 19:
  print("Valid pupil age")
while StuAge < 10 or StuAge > 19:
  print("Invalid input: enter a value from 10 to 18")
  StuAge = int(input("Enter age of student\n>"))

Attendance = int(input("Enter attendance percentage\n"))
Exam = int(input("Enter exam mark\n"))
Grade = "nul"

if Attendance >= 90:
  if Exam > 70:
    if Exam > 70 and Exam <=80:
      Grade = "C"
    elif Exam >80 and Exam <=90:
      Grade = "B"
    else:
      Grade = "A"
  else:
    Grade = "F"
else:
  Grade = "F"

print("The grade is " + Grade)
