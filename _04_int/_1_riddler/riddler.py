# riddle #1 I Am White When Dirty And Black When Clean answer a chalk board
# ridlle #2 What has six faces, but does not wear makeup, has twenty-one eyes, but cannot see? answer dice
# riddle #3 The more you take, the more you leave behind. answers you take steps and leave footprints
"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""

from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
   window.withdraw()
    score = 0
    riddle_1 = simpledialog.askstring(title= "The Riddle Game", prompt= "I am white when I'm dirty and black \n when I'm clean. What am I?")
    if riddle_1 == "a chalkboard":
        messagebox.showinfo(message= "correct")
        score = score + 1
    else:
        messagebox.showinfo(message= "Incorrect. A chalkboard.")
    riddle_2 = simpledialog.askstring(title= "The Riddle Game", prompt= "The more you take, the more you leave behind.")
    if riddle_2 == "steps and footprints":
        messagebox.showinfo(message= "correct")
        score = score + 1
    else:
        messagebox.showinfo(message= "Incorrect. steps and footprints.")
    riddle_3 = simpledialog.askstring(title= "The Riddle Game", prompt= "What has six faces, but does not wear \n makeup, has twenty-one eyes, but cannot see?")
    if riddle_3 == "a dice":
        messagebox.showinfo(message= "correct")
        score = score + 1
    else:
        messagebox.showinfo(message= "Incorrect. A dice.")

    messagebox.showinfo(message= "your score was " +str(score)+"/3")
    window.mainloop
