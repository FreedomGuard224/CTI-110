# CTI - 110
# P4T2: Bug Collector
# Gonzales, Edmund
# 6/27/18

def main():
    
    total = 0
    
    for day in range (1, 8):
        # Prompt the user.
        print("Enter the bugs collected on day",day)
        #Input the number of bugs.
        bugs = int(input())
        # Add bugs to total
        total = total + bugs

    # Display the total bugs.
    print("You collected a total of",total,"bugs.")

main()
    
