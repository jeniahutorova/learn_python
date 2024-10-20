from tkinter import *

window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)

image = PhotoImage(file="/Users/jane/learn_python/day_26/logo.png")
canvas = Canvas(width=240, height=240, highlightthickness=0)
canvas.create_image(120, 120, image=image)
canvas.grid(row=0, column=1)

website_label = Label(window, text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(window, text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(window, text="Password:")
password_label.grid(row=3, column=0)

website_input = Entry(window, text="", width=35)
website_input.grid(row=1,column=1,columnspan=2)

email_input = Entry(window, text="", width=35)
email_input.grid(row=2,column=1,columnspan=2)

password_input = Entry(window, text="", width=21)
password_input.grid(row=3,column=1)

generate_btn = Button(window, text="Generate password")
generate_btn.grid(row=3,column=2)

add_btn = Button(window, text="Add",width=36)
add_btn.grid(row=4, column=1, columnspan=2)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window.mainloop()