# CTI-110
# P4 Lab 2: Initials
# Gonzales, Edmund
# 06/27/18

def main():

    import turtle

    turtle.shape("turtle")
    t = turtle
    t.color("green")
    t.pensize(10)

    #assigned letters according to first letter of number
    #except for 25 where t was already assigned to turtle. "to" was used. 
    o = 180
    n = 90
    s = 75
    f = 50
    to = 25

    #First Initial
    def first():
        for first in [1,2]:
            t.backward(f)
            t.right(n)
            t.forward(f)
            t.left(n)
            t.forward(f)
            
    #Stamp after E and repositioning for beginning of G
    def middle():
        t.penup()
        t.forward(to)
        t.stamp()
        t.forward(n)
        t.left(n)
        t.forward(f)
        t.right(n)
        t.pendown()
        
    #Beginning of G and the three sections of G to make it look neat
    def second():
        t.forward(f)
        t.right(n)
        
        for second in range (1,6):
            t.forward(22)
            t.right(28)

        for secondtwo in range (1,6):
            t.forward(22)
            t.right(20)

        for secondthird in range (1,4):
            t.forward(22)
            t.right(28)
            
    #Resting place for the turtle to simulate the stamp after E        
    def last():
        t.penup()
        t.right(35)
        t.forward(103)
        t.left(n)
        t.forward(to)
            
    first()
    middle()
    second()
    last()
    
main()
