# CTI-110 
# P3HW1 - Age Classifier 
# Gonzales Edmund 
# 6/19/18

#Define task
print("Your stage of life will be shown.")

#Get information from user
age=int(input("What is your age?"))

#Designate a category
def main():
    if age <= 1:
        print("You are an infant.")
    elif age <= 12:
        print("You are a child.")
    elif age <= 19:
        print("You are a teenager.")
    elif age >= 20:
        print("You are an adult.")

#Run the main code        
main()
           
