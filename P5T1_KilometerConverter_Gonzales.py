# CTI 110
# P5T1: Kilometer Converter
# Gonzales, Edmund
# 7/4/18

conversion_factor = 0.6214

def main():
    
    kilometers = float(input("Enter a distance in kilometers: "))

    show_miles(kilometers)

def show_miles(km):
    
    miles = km * conversion_factor
    print(km, "kilomters equals",format(miles,".2f"),"miles.") 


main()

