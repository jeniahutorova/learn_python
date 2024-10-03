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
my_label.pack()

button = Button(window, text = "Click me", command=button_clicked)
button.pack()

input = Entry()
input.pack()
# Start the GUI event loop
window.mainloop()