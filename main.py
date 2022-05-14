# Day 33 Project 1: Build a Kanye Quotes App using the Kanye Rest API


from tkinter import *
import requests


# TODO 2. EXTRACT TEXT FROM URL
def get_quote():
    respond = requests.get(url="https://api.kanye.rest")
    data = respond.json()
    respond.raise_for_status()
    quote = data["quote"]
    print(data)
    print(quote)
    return quote

def update_quote():
    new_quote = get_quote()
    canvas_back.itemconfig(quote_text, text=new_quote)


# TODO 1. SET UP THE INTERFACE
window = Tk()
window.title("Kanye Qutoes App")
window.config(padx=50, pady=50)

canvas_back = Canvas(height=414, width=300)
background_image = PhotoImage(file="background.png")
canvas_back.create_image(150,207, image=background_image)
canvas_back.grid(column=1, row=1)


# TODO 3. SET UP CANVAS FOR THE QUOTES WHICH IS IN THE CANVAS_BACK
quote = get_quote()
quote_text = canvas_back.create_text(150,170,text=quote,  width=250, font=("Arial", 30, "bold"), fill="white")

# TODO 4. SET UP THE BUTTON WHICH COULD UODATE THE QUTOES
kanye_image = PhotoImage(file="kanye.png")
button = Button(image=kanye_image, highlightthickness=0, command=update_quote)
button.grid(column=1, row=2)

window.mainloop()