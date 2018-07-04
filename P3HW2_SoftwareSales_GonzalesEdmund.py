# CTI-110 
# P3HW2 - Software Sales 
# Gonzales Edmund 
# 6/19/18

#Define Task
print("Based off of the number of packages purchased, we " + \
      "will give you the total cost to include discounts.")

#Define variables
#rC = retail cost
rC = 99 

#Get user information
#tP = total purchased
tP=float(input("How many packages did you purchase? "))

#Calculate initial cost
#iC = initial cost
iC = rC*tP
print("The total cost before the discount is $",format(iC,".2f"))

#Calculate discount
def main():
    if tP <= 9:
        print("With a 0% discount, the total amount comes out to $",format(iC,".2f"))
    elif tP <=19:
        tenDiscount = iC * .90
        print("With a 10% discount, the total amount comes out to $",format(tenDiscount,".2f"))
    elif tP <=49:
        twentyDiscount = iC * .80
        print("With a 20% discount, the total amount comes out to $",format(twentyDiscount,".2f"))
    elif tP <=99:
        thirtyDiscount = iC * .70
        print("With a 30% discount, the total amount comes out to $",format(thirtyDiscount,".2f"))
    elif tP >=100:
        fortyDiscount = iC * .60
        print("With a 40% discount, the total amount comes out to $",format(fortyDiscount,".2f"))
main()
