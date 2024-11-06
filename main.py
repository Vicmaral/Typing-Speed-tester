import customtkinter
import tkinter as tk
import time
from random_word import RandomWords

customtkinter.set_appearance_mode("light")
WHITE = "#ffffff"
BLACK = "#000000"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
h_size = 800
w_size = 1200


def get_random_word():
    r = RandomWords()
    temp_word=r.get_random_word()
    while len(temp_word)>5:
        temp_word=r.get_random_word()
    return temp_word


# global typed_word, random_word, num_words
typed_word = ""
random_word = get_random_word()
num_words = 0
num_chars = 0
start = 0


def key_pressed(event):
    global random_word, num_chars, typed_word, num_words, start
    if start == 0:
        start = time.time()
    if event.keysym == 'BackSpace':
        typed_word = typed_word[:-1]
    else:
        typed_word += "".join((event.char,))
    if typed_word == random_word:
        num_words += 1
        num_chars += len(random_word)
        random_word = get_random_word()
        word_to_type.config(text=random_word)
        typed_word = ''
        output_word.config(text=typed_word)
        entry.delete(0, customtkinter.END)
        tk.Label(window, text="  Words:" + str(num_words), font=(FONT_NAME, 20, 'bold')
                 ).grid(row=4, column=2)
        tk.Label(window, text="  " + str(round((num_words / (time.time() - start) * 60), 2)) + "words/s  ",
                 font=(FONT_NAME, 20, 'bold')
                 ).grid(row=4, column=1)
        tk.Label(window, text=str(round((num_chars / (time.time() - start) * 60), 2)) + "chars/s  ",
                 font=(FONT_NAME, 20, 'bold')
                 ).grid(row=4, column=0)
    else:

        print('You pressed %s\n' % typed_word)
        output_word.config(text=typed_word)


#Create windows
window = customtkinter.CTk()
window.title("Typing Speed Tester")
window.config(height=h_size, width=w_size, bg=YELLOW)

# Draw Tittle
title = customtkinter.CTkLabel(window, text="Typing Speed Tester", font=(FONT_NAME, 40, 'bold'), fg_color=YELLOW,
                               ).grid(row=0, column=1, columnspan=2)
word_to_type = tk.Label(window, text=random_word, font=(FONT_NAME, 20, 'bold'))
word_to_type.grid(row=1, column=1, columnspan=2)

entry = customtkinter.CTkEntry(window, height=2, width=100)
entry.grid(row=2, column=1, columnspan=3)

output_word = tk.Label(window, text=typed_word, font=(FONT_NAME, 20, 'bold'))
output_word.grid(row=3, column=1, columnspan=2)

window.bind('<KeyPress>', key_pressed)

window.mainloop()
