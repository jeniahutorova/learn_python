from tkinter import *

def button_clicked():
    tb_data = entry.get()
    terabytes = float(tb_data)
    bytes_data = round(terabytes * 1099511627776)
    b_conversion.config(text = str(bytes_data))

window = Tk()
window.title("Bytes to Terabytes Calculator")
window.minsize(300, 200)
window.config(padx=50, pady=50)

entry = Entry()
entry.grid(column=2, row=1)

tb_label = Label(window, text="Terabytes")
tb_label.grid(column=3, row=1)

bytes_label = Label(window, text="Bytes")
bytes_label.grid(column=3, row=2)

b_conversion = Label(window, text="")
b_conversion.grid(column=2, row=2)

eq_label =Label(window, text="is equal to")
eq_label.grid(column=1, row=2)

button = Button(window, text="Calculate", command=button_clicked)
button.grid(column=2, row=3)

window.mainloop()