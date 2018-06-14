# CTI-110 
# P2HW2 - Tip Tax Total 
# Gonzales Edmund
# 13/6/18

foodCost = float(input("What is the charge for the meal?"))
tipAmount = .18*foodCost
print("A tip of 18% comes out to $",format(tipAmount,",.2f"))
salesTax=.07*foodCost
print("A sales tax of 7% comes out to $",format(salesTax,",.2f"))
totalCost=foodCost+tipAmount+salesTax
print("The total cost of the meal with tip amount and sales tax is $",format(totalCost,",.2f"))
