# CTI - 110
# P4HW1: Distance Traveled
# Gonzales, Edmund
# 6/28/18

def main():

    count = 0
    hour = 0

    speed = int(input("How many mph was the vehicle traveling? "))
    time = int(input("How many hours was the vehicle traveling for? "))

    print()
    print("Hours".ljust(10) + "Distance Traveled".ljust(18))
    print("-"*30)
    
    while count != time:
        count = count + 1
        hour = hour + 1
        travel = speed * count
        print(hour," "*7,travel)
       
main()
