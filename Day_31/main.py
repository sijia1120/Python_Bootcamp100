from tkinter import *
import pandas
import random
import time
# BACKGROUND COLOR
BACKGROUND_COLIR = "#B1DDC6"
FONT1= ("Ariel",35,"italic")
FONT2= ("Ariel",55,"bold")
random_card = {}
remember_dict ={}
forgotten_dict = {}
final_dict = {}

## TODO 2. CREATE NEW FLASH CARDS

try:
    with open("words_to_learn.csv","w") as file:
        data = pandas.read_csv(file)
except:
    print("cant find")
    with open("french_words.csv","r") as file:
        data = pandas.read_csv(file)
finally:
    word_dict = {row["French"]: row["English"] for (index, row) in data.iterrows()}
    french = [row["French"] for (index, row) in data.iterrows()]
    all_french = [row["French"] for (index, row) in data.iterrows()]



def random_pick():
    global flip_timer
    window.after_cancel(flip_timer)
    global random_card
    random_card = random.choice(french)
    canvas.itemconfigure(background, image=front_image)
    canvas.itemconfigure(can_word,text=random_card, fill="black")
    canvas.itemconfigure(can_title,text="French", fill="black")
    flip_timer = window.after(3000, func=show_eng)


def show_eng():
    global random_card
    canvas.itemconfigure(background,image=back_image)
    canvas.itemconfigure(can_word, text= word_dict[random_card], fill="white")
    canvas.itemconfigure(can_title,text="English",fill="white")

def yes_button():
    global random_card
    global all_french
    global remember_dict
    remember_dict[random_card] = word_dict[random_card]

    final = word_dict.keys() - remember_dict.keys()
    final = list(final)
    global final_dict
    final_dict ={ n:word_dict[n] for n in final}

    data= pandas.DataFrame.from_dict(final_dict, orient="index")
    data.to_csv("words_to_learn.csv")

    random_pick()

def no_button():
    global random_card
    global forgotten_dict
    forgotten_dict[random_card] = word_dict[random_card]
    print(forgotten_dict)
    random_pick()

##### TODO 1.SET UP THE GUI WINDOW
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50,bg=BACKGROUND_COLIR)

flip_timer = window.after(3000, func=show_eng)

# Greate the Canvas
canvas = Canvas(height=526, width=800)
front_image= PhotoImage(file="card_front.png")
back_image = PhotoImage(file="card_back.png")
background = canvas.create_image(400,263, image=front_image)

# Add texts on the canvas
can_title = canvas.create_text(400,150,text="Title", font=FONT1)
can_word = canvas.create_text(400,300,text="word",font=FONT2)

canvas.config(bg=BACKGROUND_COLIR, highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)

# Button create for checking right and wrong
right_image = PhotoImage(file="right.png")
right_image= right_image.zoom(3,3)
right_image= right_image.subsample(5,5)
wrong_image = PhotoImage(file="wrong.png")
wrong_image= wrong_image.zoom(3,3)
wrong_image= wrong_image.subsample(5,5)

right= Button(image=right_image,highlightthickness=0,bg=BACKGROUND_COLIR, command=yes_button)
right.grid(column=0, row=1)
wrong= Button(image=wrong_image,highlightthickness=0,bg=BACKGROUND_COLIR, command=no_button)
wrong.grid(column=1, row=1)

random_pick()

window.mainloop()

