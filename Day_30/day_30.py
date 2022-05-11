# This is a sample Python script.
from tkinter import *
from tkinter import messagebox
import random
import json
import pyperclip

### SEARCH FINCTION
def search():
    website = entry_wb.get()
    with open("data.json","r") as search_file:
        data = json.load(search_file)

        for item in data:
            if item == website:
                email = data[item]["email"]
                password = data[item]["password"]
                messagebox.showinfo(title="Search password", message=f"Email: {email}\nPassword: {password}")
            else:
                print(f"You have not created password for {website}")
                messagebox.showinfo(title="Search password", message = f"You have not created password for {website}")
                break



#### PASSWORD GENERATOR
def generator():
    letters ="abcdefjhijklmnopqrstuvwxyz"
    letter =[n for n in letters]
    numbers ="0123456789"
    number = [n for n in numbers]
    symbol =["!","£","$","%","^","&","*","(",")","_","+"]
    nr_letter = [ random.choice(letter) for n in range(random.randint(8,10))]
    nr_number = [ random.choice(number) for n in range(random.randint(2,4))]
    nr_symbol = [random.choice(symbol) for n in range(random.randint(2,4))]

    password_list =nr_letter + nr_number + nr_symbol
    random.shuffle(password_list)
    password = "".join(password_list)

    entry_pw.insert(0,password)
    pyperclip.copy(password)

#### SAVE PASSWORD
def add():
    website = entry_wb.get()
    password = entry_pw.get()
    email = entry_user.get()

    new_data = {
        website: {
            "email":email,
            "password": password,
        }
    }

    if len(website)==0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please ensure there is no information empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                #Reading old data

        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            entry_wb.delete(0, END)
            entry_pw.delete(0, END)

#### UI SETPUP
window = Tk()
window.title("Password Generator")
window.config(padx= 50, pady=50)

canvas = Canvas(height=180,width=180)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image= password_image)
canvas.grid(column=1, row=1)

###Entry for Website:
entry_wb = Entry(width=28)
### Insert: inserts text at the given index. Use insert(INSERT,text)
# to insert text at the cursor, insert(END, text) to append text to the widget
entry_wb.insert(0, string="")
entry_wb.grid(sticky =W,column=1, row=2)
entry_wb.focus() # which makses the curse at the website entry

###Entry for Username/Email
entry_user = Entry(width=50)
entry_user.insert(END, string="sijia1120@gmail.com")
print(entry_user.get())
entry_user.grid(sticky =W,column=1, row=3, columnspan=2)

###Entry for password
entry_pw =Entry(width=28,justify= LEFT)
entry_pw.insert(END, string="")
print(entry_pw.get())
######## sticky = W makes the Label on the left
entry_pw.grid(sticky ="NW",column=1, row=4, columnspan=1)

###Label for websites
label_wb= Label(text="Websits:   ", font=("bold"))
label_wb.grid(sticky =W,column= 0, row=2)

###Label for Email/ Usernames
label_wb= Label(text="Email/ Usernames:   ", font=("bold"))
label_wb.grid(sticky =W,column= 0, row=3)

###Label for Password
label_wb= Label(text="Password:   ", font=("bold"))
label_wb.grid(sticky =W,column= 0, row=4)

# Create button for Add
add = Button(text="Add", width=42,command=add)
add.grid(sticky =W,column=1, row=5, columnspan=2)

# Create button for Generate Password
add = Button(text="Generate Password", width=16, command=generator)
add.grid(sticky="NW",column=2, row=4)

# search button
search_button = Button(text="Search",width=15, command=search)
search_button.grid(column=2, row=2)



window.mainloop()
