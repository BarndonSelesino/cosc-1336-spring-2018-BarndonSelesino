#write the import statements to bring in homework 4 functions
#valid_letter_grade, get_credit_points, get_grade_points, and get_grade_point_average
from src.homework.homework4 import (valid_letter_grade, get_credit_points,get_grade_points,get_grade_point_average)

'''
Use the functions from homework4 to...
Write code to prompt the user for number of students and grades.
Create a nested loop to collect letter grades and credit hours for each student.
Vaidate the letter grade is in accepted range if not prompt user for letter again.
From the letter grade, get the credit points for that class.
Calculate grade points (How? Research GPA calculation).
Sum grade points and credit hours for each student.
Calculate GPA for each student.
Display Student 1(etc) GPA is 3.77. Format the GPA to two values.
'''

#WRITE YOUR CODE IN THE MAIN FUNCTION BELOW
def main():
    number_of_students = int(input('Please enter the number of students:      '))
    credit_s = 0
    gpa2 = 0

#class selection
    classes = int(input('How many classes did the students take?'))
    credit_s = 0
    gpa2 = 0

#grade selection
    for v in range(1, classes+1):
        entered_grade = (input('Please enter letter grade ' +str(v) + ':' )
        while valid_letter_grade(str(entered_grade)) != True:
            entered_grade = input('Enter a valid grade: (A,B,C,D, or F):     ')
#conclusion of program
        entered_grade = get_credit_points(entered_grade)
        credit_hours = int(input('How many credits was the class ' + str(v)))
        credit_s += credit_hours
        grade_points = get_grade_points(credit_hours,entered_grade)
        gpa2 += grade_points
    
    gpa = get_grade_point_average(credit_s,gpa2)
    print('the student ' +str(q) + 's gpa is:  ' + "%.2f" % gpa)                       
                           
                    
                            
                    
main()

#CALL THE MAIN FUNCTION


