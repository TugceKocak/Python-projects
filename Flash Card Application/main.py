from tkinter import *
import random
import pandas
import os

BACKGROUND_COLOR = "#B1DDC6"

window=Tk()
window.title("Flash Card")
window.config(padx=50, pady=20, bg=BACKGROUND_COLOR)

if os.path.exists('words_to_learn.csv'):
    dataframe=pandas.read_csv("words_to_learn.csv")
else:
    dataframe=pandas.read_csv("english_words.csv")

dict=dataframe.to_dict('records')
sample=random.choice(dict)

canvas=Canvas(window, width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front=PhotoImage(file="card_front.png")
card_back=PhotoImage(file="card_back.png")
canvas_image=canvas.create_image(400, 263, image=card_front )
title_text=canvas.create_text(400,150,text="English",fill="black",font=("Arial",30,"italic"),anchor=CENTER)
word_text=canvas.create_text(400,263,text=sample['English meaning(s)'],fill="black",font=("Arial",50,"bold"),anchor=CENTER)
canvas.pack()
canvas.grid(column=0,row=0,columnspan=2)

def flipCard():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(word_text, text=sample['Turkish'],fill="white")
    canvas.itemconfig(title_text, text="Türkçe",fill="white")
    window.after_cancel(timer)

timer=window.after(3000, flipCard)

def changeword():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(title_text, text="English", fill="black")
    global sample
    sample = random.choice(dict)
    canvas.itemconfig(word_text, text=sample['English meaning(s)'],fill="black")
    timer=window.after(3000, flipCard)

def clickRight():
    global dict
    dict.remove(sample)
    df = pandas.DataFrame(dict)
    df.to_csv('words_to_learn.csv', index=False, encoding='utf-8-sig')
    changeword()

my_image1 = PhotoImage(file="wrong.png")
button1 = Button(image=my_image1, highlightthickness=0, command=changeword)
button1.grid(column=0, row=1)

my_image2 = PhotoImage(file="right.png")
button2 = Button(image=my_image2, highlightthickness=0, command=clickRight)
button2.grid(column=1, row=1)

print(dict)

window.mainloop()