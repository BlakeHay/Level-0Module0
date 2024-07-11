# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr
from tkinter import messagebox, simpledialog, Tk
import math
if __name__ == '__main__':
    window = Tk()
    radius = simpledialog.askinteger(title= "Circle Calculator", prompt= "Please enter a radius of a circle")
    use = simpledialog.askstring(title= " circle Calculator", prompt="Would you like your calculation to be circumference or area.")
    area = radius * radius * math.pi
    circumferemce = radius * math.pi * 2
    if use == "circumference":
        messagebox.showinfo(message= "The circumference is "+ str(circumferemce)+".")
    if use == "area":
        messagebox.showinfo(message= "The area is "+ str(area)+".")
    window.mainloop






