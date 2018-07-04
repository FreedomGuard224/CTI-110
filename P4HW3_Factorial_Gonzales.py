# CTI - 110
# P4HW3: Factorial
# Gonzales, Edmund
# 7/1/18

def main():
    
    originNum = int(input("Enter a number: "))

    while originNum<= -1:
        originNum = int(input("Enter a positive number "))

    x = originNum
 
    y= x - 1 
    z = x * y
    x = x-2
    
    while x > 0:
        z = z * x
        x = x - 1

    if originNum == 0:
        print("The factorial of 0 is 1")
    elif originNum == 1:
        print("The factorial of 1 is 1")
    else:
        print("The factorial of",originNum,"is ",z)

main()
