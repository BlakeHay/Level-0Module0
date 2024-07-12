"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
from tkinter import messagebox, simpledialog, Tk

def adder( number1, number2):
    return number1 + number2

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    x = simpledialog.askinteger(title= " ", prompt= "Choose a random number.")
    y = simpledialog.askinteger(title= " ", prompt= "Choose another random number.")
    num = adder(x,y)
    messagebox.showinfo(message= "The sum is " + str(num)+ ".")














































