"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""

def calculator( num1, num2, opr):
    if opr == "addition":
        return num1 + num2
    if opr == "subtraction":
        return num1 - num2
    if opr == "multiplication":
        return num1 * num2
    if opr == "division":
        return num1/num2


from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw
    number1 = simpledialog.askinteger(title= "Calculator", prompt= "I am a calculator. What is your first number?")
    number2 = simpledialog.askinteger(title= "Calculator", prompt="What is your second number?")
    operation = simpledialog.askstring(title="Calculator", prompt= "What operation would you like me to do?")
    output = calculator(number1, number2, operation)
    messagebox.showinfo(message= "If my calculations are correct the answer is " + str(output)+ "." )

    window.mainloop()


