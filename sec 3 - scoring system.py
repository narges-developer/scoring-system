# ===========================================
# Project: Student Grading System
# Description:
# This program receives a student's name and
# score, validates the input, assigns a letter
# grade, determines the academic status, and
# displays a formatted report card.
#
# Concepts Used:
# - Variables
# - Input
# - if / elif / else
# - Comparison Operators
# - Logical Operators
# ===========================================
student_name = input("Enter the student's name : ")
grade = float (input("Enter your grade : "))
if 0 <= grade <=100 :
    if 90 <= grade  : 
        letter = "A"
        result = "Excellent!"
    elif 80 <= grade :
        letter = "B"
        result = "Very Good!"
    elif 70 <= grade :
        letter = "C"
        result = "Good!"
    elif 60 <= grade :
        letter = "D"
        result = "Needs Improvement!"
    else :
        letter = "F"
        result = "Failed!"
    if grade > 60 :
        status = "Passed!"
    else : 
        status = "Failed!"
    print("""
    =.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=
             REPORT CARD
    =.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=
    """)       
    print("Student's name : " , student_name)
    print("Student Grade : ", grade)
    print("Letter Grade : ", letter)
    print("Result : ", result )
    print("Academic status : ", status)
    print("""
    =.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=
      """)
else : 
    print("""Invalid grade.
Please enter a number between 0 and 100.""") 
input()