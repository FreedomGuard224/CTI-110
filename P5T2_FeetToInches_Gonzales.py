# CTI - 110
# P5T2: Feet to Inches
# Gonzales, Edmund
# 7/4/18

inches_per_foot = 12

def main():
    
    feet = int(input("Enter a number of feet: "))

    print(feet, "equals", feet_to_inches(feet), "inches.")
    

def feet_to_inches(feet):
    return feet * inches_per_foot

main()


    
