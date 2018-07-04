# CTI - 110
# P5HW1: Test Average and Grades
# Gonzales, Edmund
# 7/4/18

def main():
  
    totalGrade = 0

    print("Enter 5 test grades.")

    for x in range (5):
        grade = int(input("Enter grade:"))
        totalGrade = totalGrade + grade
        determine_grade(grade)

    print("The average of these 5 grades is",calc_average(totalGrade))

def calc_average(totalGrade):
    average = totalGrade / 5
    return average
    

def determine_grade(grade):

    if grade >= 90 and grade <= 100:
        print("The letter grade of",grade,"is A.")
    elif grade >= 80 and grade <= 89:
        print("The letter grade of",grade,"is B.")
    elif grade >= 70 and grade <= 79:
        print("The letter grade of",grade,"is C.")
    elif grade >= 60 and grade <= 69:
        print("The letter grade of",grade,"is D.")
    elif grade >= 0 and grade <= 59:
        print("The letter grade of",grade,"is F.")
    
main()















##    grade1 = int(input("Enter grade 1: "))
##    totalGrade = totalGrade + grade1
##    grade2 = int(input("Enter grade 2: "))
##    totalGrade = totalGrade + grade2
##    grade3 = int(input("Enter grade 3: "))
##    totalGrade = totalGrade + grade3
##    grade4 = int(input("Enter grade 4: "))
##    totalGrade = totalGrade + grade4
##    grade5 = int(input("Enter grade 5: "))
##    totalGrade = totalGrade + grade5
    

