import tkinter


window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(500, 300)



my_label = tkinter.Label(window, text ="I\'m a label", font =("Arial", 24, "bold"))
my_label.pack()
window.mainloop()