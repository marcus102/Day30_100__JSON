from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

FONT_NAME = 'Courier'
FONT_TYPE = 'bold'
SIZE = 10

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_letters = [choice(letters) for _ in range(randint(8, 10))]
  password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
  password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
  password_list = password_letters + password_symbols + password_numbers

  shuffle(password_list)

  password = ''.join(password_list)

  password_input.insert( 0, password)
  pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def search_data():
  try:
    with open ('data.json', 'r') as data:
      my_data = json.load(data)
  except FileNotFoundError:
    is_ok = messagebox.askokcancel(title='Location Error', message="File Path doesn't exist\nCreate A file adn store your info")
    if is_ok:
      generate_password()
      save_infos()
  else:
    if website_input.get() in my_data:
      messagebox.showinfo(title=f"{website_input.get()}", message=f"Email: {my_data[website_input.get()]['email']}\nPassword: {my_data[website_input.get()]['password']}")
      website_input.delete(0, END)
      website_input.focus()
    else:
      is_ok = messagebox.askokcancel(title='Website not found!', message=f"{website_input.get()} does't exist!\nDo you want to add it?")
      if is_ok:
        generate_password()
        save_infos()
        messagebox.showinfo(title='Message', message='Added Successfuly!')
      else:
        website_input.delete(0, END)
        website_input.focus()
  
          
def save_infos():
  
  new_data = {
    website_input.get(): {
    'email': username_input.get(),
    'password': password_input.get(),
  }
  }
  
  if len(website_input.get()) == 0 or len(password_input.get()) == 0:
    messagebox.showwarning(title='Error!', message='Empty Input!\nmake sure to fill the form')
  else:
    # is_ok = messagebox.askokcancel(title=website_input.get(), message=f'These are the details entered: \n Email: {username_input.get()}\n Password: {password_input.get()}\n Would you like to save it?')
    # if is_ok:
  
    # with open ('data.json', 'w') as data:
      # json.dump(new_data, data, indent=2)
    # with open ('data.json', 'r') as data:
      # print(json.load(data))
    try:
      with open ('data.json', 'r') as data:
        my_data = json.load(data)
    except FileNotFoundError:
      with open ('data.json', 'w') as data_file:
        json.dump(new_data, data_file, indent=2)
    else:
      my_data.update(new_data)
      with open ('data.json', 'w') as data:
        json.dump(my_data, data, indent=2)
    finally: 
      website_input.delete(0, END)
      password_input.delete(0, END)
      website_input.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

lock_img = PhotoImage(file='logo.png')

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image= lock_img)
canvas.grid(column=1, row=0)

#LABELS
website = Label(text='Website: ', font=(FONT_NAME, SIZE, FONT_TYPE))
website.grid(column=0, row=1)

user_name = Label(text='Email/Username: ', font=(FONT_NAME, SIZE, FONT_TYPE))
user_name.grid(column=0, row=2)

password = Label(text='Password: ', font=(FONT_NAME, SIZE, FONT_TYPE))
password.grid(column=0, row=3)

#ENTRY
website_input= Entry(width=40)
website_input.grid(column=1, row=1, columnspan=2)
website_input.config(borderwidth=0)
website_input.focus()

username_input= Entry(width=40)
username_input.grid(column=1, row=2, columnspan=2)
username_input.config(borderwidth=0)
username_input.insert( 0, 'marcus@gmail.com')

password_input= Entry( width=21)
password_input.grid(row=3, column=1)
password_input.config(borderwidth=0)

#BUTTON
pass_gen = Button(text='Generate Password', command=generate_password)
pass_gen.grid(row=3, column=2)
pass_gen.config(borderwidth=0, fg='blue')

pass_gen = Button(text='Add', width=40, font=(FONT_NAME, SIZE, FONT_TYPE), command=save_infos)
pass_gen.grid(column=1, row=4, columnspan=2)
pass_gen.config(borderwidth=0, fg='green')

search = Button(text='Search', width=5, command=search_data)
search.grid(row=1, column=2)
search.config(borderwidth=0, fg='orange')

window.mainloop()