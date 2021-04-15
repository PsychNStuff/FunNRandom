# open Tkinter and time data in Python
from tkinter import *
from time import strftime

app_window = Tk()
app_window.title("My Digital Time")
app_window.geometry("350x150")
app_window.resizable(0, 0)

# Text design; feel free to edit, but if you edit this, also edit the label
text_font = ("Calibri", 55, 'bold')
background = "#10b552"
foreground = "#d61208"
border_width = 25

# Interface
label = Label(app_window, font=("Calibri", 50, 'bold'), bg="green", fg="red", bd=25)
label.pack(anchor='center')


# Time in hours, minutes, seconds (military time). Add %p after %S for AM/PM
def digital_clock():
    time_live = strftime('%I:%M %p')
    label.config(text=time_live)
    label.after(200, digital_clock)


# Create button for next text.
button_1 = Button(app_window, text="Next", bd='5', command=app_window.destroy)

label.pack()
button_1.pack()

# Run
digital_clock()
app_window.mainloop()