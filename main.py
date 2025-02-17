import json
from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
from random import choice, randint, shuffle


def generated_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_number

    shuffle(password_list)

    password_generator = "".join(password_list)

    password_entry.insert(0, password_generator)

    pyperclip.copy(password_generator)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_entry.get()
    saved_email = email_entry.get()
    saved_password = password_entry.get()
    new_data = {
        website_name: {
            "email": saved_email,
            "password": saved_password
        }
    }

    if len(website_name) == 0 or len(saved_password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:

        is_ok = messagebox.askokcancel(title=website_name, message=f"These are the details entered: \n"
                                                                   f"Email: {saved_email}"
                                                                   f"\nPassword: {saved_password}\n Is it ok to save?")

        if is_ok:
            try:
                with open("data.json", "r") as f:
                    # Reading old data
                    data = json.load(f)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                with open("data.json", "w") as f:
                    json.dump(new_data, f, indent=4)
            else:
                # updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as f:
                    # Saving updated data
                    json.dump(data, f, indent=4)
            finally:
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_typed = website_entry.get()

    try:
        with open("data.json", "r") as file:
            data_list = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")

    else:
        if website_typed in data_list:
            email_found = data_list[website_typed]["email"]
            password_found = data_list[website_typed]["password"]
            messagebox.showinfo(title=website_typed, message=f"Email: {email_found}\n "
                                                             f"Password: {password_found}")
        else:
            messagebox.showinfo(title="Error", message="No details for the website exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)

email = Label(text="Email/Username:")
email.grid(row=2, column=0)

password = Label(text="Password:")
password.grid(row=3, column=0)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)

generate_password = Button(text="Generate Password", command=generated_password)
generate_password.grid(row=3, column=2)

add = Button(text="Add", width=36, command=save)
add.grid(row=4, column=1, columnspan=2)

website_entry = Entry(width=25)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=43)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "@gmail.com")

password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)

window.mainloop()
