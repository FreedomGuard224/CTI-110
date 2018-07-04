# CTI-110
# P4 Lab 1: Shapes
# Gonzales, Edmund
# 06/27/18

def main():
    
    import turtle

    turtle.shape("turtle")
    t = turtle
    a = 100
    b = 90
    c = 120
    
    def square():
        t.color("red")
        for square in range (0,4):
            t.forward(a)
            t.left(b)
        t.forward(a)

    def triangle():
        t.color("blue")
        t.forward(a)
        for triangle in range (0,2):
            t.left(c)
            t.forward(a)
            
    square()        
    triangle()

main()

