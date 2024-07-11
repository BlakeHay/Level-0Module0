import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    my_turtle = turtle.Turtle()
    my_turtle.speed(4)
    my_turtle.width(2)
    my_turtle.color('black')
    shape = simpledialog.askstring(title= "The Amazing Shape Maker", prompt="What shape can I draw for you.")
    if shape == "triangle":
        for a in range (3):
            my_turtle.forward(100)
            my_turtle.right(180)
    if shape == "square":
        for b in range (4):
            my_turtle.forward(100)
            my_turtle.right(90)
    if shape == "circle":
        my_turtle.circle(50)
    window.mainloop()
    turtle.done

    # Ask the user what shape they want to draw and store it in a variable
    
    # Draw the shape requested by the user using if-elif-else statements
    
    # Call the turtle .done() method
