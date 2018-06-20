# CTI-110 
# P3T1 - Areas of Rectangles
# Gonzales,Edmund
# 11/19/18

#define task
print("Compare the area of two rectangles.")

#Get information
length1 = float(input("What is the length of the 1st rectangle? "))              
width1 = float(input("What is the width of the 1st rectangle? "))            
area1 = length1*width1           
print("The area of the 1st rectangle is",format(area1,".2f"))

#Get information about the second rectangle
length2 = float(input("What is the length of the 2nd rectangle? "))            
width2 = float(input("What is the width of the 2nd rectangle? "))          
area2 = length2*width2          
print("The area of the 2nd rectangle is",format(area2,".2f"))

#compare the two rectangles
if area1 > area2:
    print("The area of the 1st rectangle is larger than the 2nd rectangle.")
elif area2 > area1:
    print ("The area of the 2nd rectangle is larger than the 1st rectangle.")
else:
    print("The rectangles have the same area.")


