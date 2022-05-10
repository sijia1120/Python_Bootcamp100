# This is a sample Python script.
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
save_dict = {}

#### PASSWORD GENERATOR
def generator():
    letters ="abcdefjhijklmnopqrstuvwxyz"
    letter =[]

    letter =[n for n in letters]
    print(letter)
    numbers ="0123456789"
    number = [n for n in numbers]
    print(number)
    symbol =["!","£","$","%","^","&","*","(",")","_","+"]
    print(symbol)

    nr_letter = [ random.choice(letter) for n in range(random.randint(8,10))]
    nr_number = [ random.choice(number) for n in range(random.randint(2,4))]
    nr_symbol = [random.choice(symbol) for n in range(random.randint(2,4))]

    password_list =nr_letter + nr_number + nr_symbol
    print(password_list)
    random.shuffle(password_list)
    print(password_list)
    password = "".join(password_list)

    print(password)

    entry_pw.insert(0,password)
    pyperclip.copy(password)

#### SAVE PASSWORD
def add():
    global save_dict
    save_dict["Website"] = entry_wb.get()
    save_dict["Password"] = entry_pw.get()
    save_dict["Username"] = entry_user.get()

    if len(save_dict["Website"])==0 or len(save_dict["Password"]) == 0:
        messagebox.showinfo(title="Oops", message="Please ensure there is no information empty!")
    else:
        is_okay = messagebox.askokcancel(title="Information confrim\n", message=f"Website:{save_dict['Website']}\n"
                                                                                f"Email:{save_dict['Username']}\n"
                                                                                f"Password:{save_dict['Password']}")
        if is_okay:
            with open("savefile.txt", mode="a") as file:
                file.write(f"{save_dict['Website']}  |  {save_dict['Username']}  |  {save_dict['Password']}\n")
                entry_wb.delete(0, END)
                entry_pw.delete(0, END)
                print(save_dict)


#### UI SETPUP
window = Tk()
window.title("Password Generator")
window.config(padx= 50, pady=50)

canvas = Canvas(height=200,width=200)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image= password_image)
canvas.grid(column=1, row=1)

###Entry for Website:
entry_wb = Entry(width=37)
### Insert: inserts text at the given index. Use insert(INSERT,text)
# to insert text at the cursor, insert(END, text) to append text to the widget
entry_wb.insert(0, string="")
entry_wb.grid(sticky =W,column=1, row=2, columnspan=2)
entry_wb.focus() # which makses the curse at the website entry
save_dict["Website"] = entry_wb.get()


###Entry for Username/Email
entry_user = Entry(width=37)
entry_user.insert(END, string="sijia1120@gmail.com")
print(entry_user.get())
entry_user.grid(sticky =W,column=1, row=3, columnspan=2)
save_dict["Username"] = entry_user.get()
print(save_dict["Username"])

###Entry for password
entry_pw =Entry(width=22,justify= LEFT)
entry_pw.insert(END, string="")
print(entry_pw.get())
######## sticky = W makes the Label on the left
entry_pw.grid(sticky ="NW",column=1, row=4, columnspan=1)
save_dict["Password"] = entry_pw.get()
print(save_dict["Password"])

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
add = Button(text="Add", width=35,command=add)
add.grid(sticky =W,column=1, row=5, columnspan=2)

# Create button for Generate Password
add = Button(text="Generate Password", width=11, command=generator)
add.grid(sticky="NW",column=2, row=4)

window.mainloop()
