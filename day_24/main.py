from tkinter import *

def button_clicked():
    data = input.get()
    my_label.config(text=data)

# Creating the main window
window = Tk()
window.title("My first GUI program")
window.minsize(500, 300)

# Create and pack lable
my_label = Label(window, text ="I\'m a label", font =("Arial", 24, "bold"))
my_label.grid(column=1, row=1)

# Create a button that will change title to an input of entry
button = Button(window, text = "Click me", command=button_clicked)
button.grid(column=2, row=2)

button = Button(window, text = "I\'m a new one", command=button_clicked)
button.grid(column=3, row=1)

# Create entry
input = Entry()
input.grid(column=4, row=3)

# Start the GUI event loop
window.mainloop()