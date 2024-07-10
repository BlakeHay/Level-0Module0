from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()


    name = simpledialog.askstring(title= " ", prompt= "What is a name you know?")
    if name == "Barak":
        messagebox.showinfo(message= "He scored 1st at his school in amc8")
    if name == "Jorje":
        messagebox.showinfo(message= "He can solve a rubix cube in undr 20 seconds.")
    if name == "Mr. C":
        messagebox.showinfo(message= "He likes to play skiing games on his phone.")

    window.mainloop()
