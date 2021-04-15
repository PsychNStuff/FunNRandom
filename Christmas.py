# Text
from tkinter import *

words = Tk()

# specify size of window.
words.title("Merry Christmas")
words.geometry("900x400")
words.resizable(0, 0)

# Text design; feel free to edit, but if you edit this, also edit the label
text_font = ("Calibri", 15, 'bold')
background = "#d61208"
foreground = "#3fe22d"
border_width = 25

# Create text widget and specify size.
text = Text(words, height=5, width=52, font=("Calibri", 15, 'bold'), bg="red", fg="green", bd=25)

# Create label
label = Label(words, font=("Calibri", 35, 'bold'), bg="green", fg="red", bd=25, text="Merry Christmas")
label.pack(anchor='center')
label.config(font=("Calibri", 35))

# Create Message
Fact = 'Wishing you a joyous Christmas this year from one coding \n nerd to another. \n With love, \n Name'

# Insert The Fact.
text.insert(END, Fact)

# Create an Exit button.
button_2 = Button(words, text="Next", bd='5', command=words.destroy)

label.pack()
text.pack()
button_2.pack()

words.mainloop()

# End program
sys.exit()
