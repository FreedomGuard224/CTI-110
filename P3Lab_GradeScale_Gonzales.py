# CTI-110 
# P3 Lab 
# Gonzales Edmund
# 6/24/18

def main():
    # This program takes a number grade and outputs a letter grade.
    # system uses 10-point grading scale
    # TO DO: define the rest of the scores
  
    #Get information from user
    score =  int(input("Enter grade: "))
    
    #Do calculations
    if score >= 90 and score <= 100:
        print("Your grade is: A")
    elif score >= 80 and score <= 89:
        print("Your grade is: B")
    elif score >= 70 and score <= 79:
        print("Your grade is: C")
    elif score >= 60 and score <= 69:
        print("Your grade is: D")
    else:
        print("Your grade is: F")

    # program start
main()
