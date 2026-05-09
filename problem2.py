"""
Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user.
"""

marks1 = int(input("Enter marks of sub 1: "))
marks2 = int(input("Enter marks of sub 2: "))
marks3 = int(input("Enter marks of sub 3: "))

percentage = ((marks1+marks2+marks3)*100)/300

if percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33:
    print("you're passed, congo. Here is your percentage:", percentage)

elif marks1<33 or marks2<33 or marks3<33:
    print("you're failed because of less than 33 marks in a subject, sorry. Here is your percentage:", percentage)
else:
    print("you're failed because total percentage is less than 40, sorry. Here is your percentage:", percentage)