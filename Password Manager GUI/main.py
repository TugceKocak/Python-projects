from contextlib import nullcontext
from tkinter import *
from tkinter import messagebox
import random
import json

def save_data():
    web=web_entry.get()
    user=username_entry.get()
    passw=pw_entry.get()
    new_data={
        web:{
            "email":user,
            "password":passw,
        }
    }
    if web=="" or user=="" or passw=="":
        messagebox.showinfo("Oops","Please don't leave any fields empty!",icon='warning')
    else:
        is_ok=messagebox.askokcancel(title=web, message="Is it ok to save data?")
        if is_ok:
            try:
                with open("data.json","r") as file:
                    data=json.load(file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open("data.json","w") as file:
                    json.dump(data,file,indent=4)
            finally:
                web_entry.delete(0,END)
                pw_entry.delete(0,END)
def search():
    try:
        with open("data.json","r") as file:
            data=json.load(open("data.json"))
            mail=f"{data[web_entry.get()].get('email')}"
            password=f"{data[web_entry.get()].get('password')}"
            messagebox.showinfo(title=web_entry.get(), message=f"Email: {mail}\nPassword: {password}")
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File found.")
    except KeyError:
        print("You dont have account!")

def generate_password(password=None):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 3)
    nr_numbers = random.randint(2, 3)

    password_list = []

    [password_list.append(random.choice(letters)) for _ in range(nr_letters)]
    [password_list.append(random.choice(symbols)) for _ in range(nr_symbols)]
    [password_list.append(random.choice(numbers)) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password=''.join(password_list)
    print(f"Your password is: {password}")
    pw_entry.delete(0,END)
    pw_entry.insert(0, password)
window=Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas=Canvas(window, width=200, height=200, highlightthickness=2)
img=PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.pack()
canvas.grid(column=1, row=0)

website_label=Label(window, text='Website:')
website_label.grid(column=0, row=1)

username_label=Label(window, text='Email/Username:')
username_label.grid(column=0, row=2)

password_label=Label(window, text='Password:')
password_label.grid(column=0, row=3)

web_entry= Entry(width=35)
web_entry.grid(column=1, row=1)
web_entry.focus()

search_button=Button(text="Search", width=15, command=search)
search_button.grid(column=2, row=1)

username_entry= Entry(width=55)
username_entry.grid(column=1, row=2, columnspan=2)

pw_entry= Entry(width=35)
pw_entry.grid(column=1, row=3)

generate_pw_button=Button(text="Generate Password", width=15, command=generate_password)
generate_pw_button.grid(column=2, row=3)

add_button=Button(text="Add", width=47, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()