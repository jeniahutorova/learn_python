from tkinter import *
def button_clicked():
    miles_data = entry.get()
    miles = float(miles_data)
    km_data = round(miles * 1.609)
    km_conversion.config(text = str(km_data))

window = Tk()
window.title("Miles to Km Calculator")
window.minsize(300, 400)

entry = Entry()
entry.grid(column=2, row=1)


miles_label = Label(window, text="Miles")
miles_label.grid(column=3, row=1)

km_label = Label(window, text="Km")
km_label.grid(column=3, row=2)

km_conversion = Label(window, text="")
km_conversion.grid(column=2, row=2)

eq_label =Label(window, text="is equal to")
eq_label.grid(column=1, row=2)

button = Button(window, text="Calculate", command=button_clicked)
button.grid(column=2, row=3)

