# CTI - 110
# P4HW2: Running Total
# Gonzales, Edmund
# 6/28/18

def main():

    sum = 0
    choice = 0
    number = 0
    
    while number >= choice:
        
        number = float(input("Enter a number: "))
        print()
        if number >= choice:
            sum = sum + number
        elif number <= choice:
            sum = sum
            
    print("Total: ",format(sum,".2f"))
    
main()
