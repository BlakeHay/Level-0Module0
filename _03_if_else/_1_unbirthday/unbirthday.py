from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    birthday = simpledialog.askstring(title= " ", prompt= " When is your birthday?")
    if birthday == "july 10":
        messagebox.showinfo(message= "Happy Birthday!")
    else:
        messagebox.showinfo(message= "Happy Unbirthday")
    window.mainloop
