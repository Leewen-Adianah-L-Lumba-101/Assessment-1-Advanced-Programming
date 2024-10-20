from tkinter import *
import tkinter as tk
import random

# Initializing variables
f1 = []             # It is generally good practice to use tuples
setup = []          # to prevent any outside function from accidentally altering the contents
punchline = []      # However, tuples are immutable, making it harder to separate the joke + punchline
char = '\n'

for line in open("randomJokes.txt"):   # This is a shorter way of accessing the contents of a text file.
    f1.append(line.split("?",1))       # 'split()' will detect the question mark from each line ONCE: (arguement '1')
                                       # then added to f1 as a separate item in a 1D array: ['joke?', 'punchline\n']. 
                                       # The 'f1' variable is a 2D array where a collection of every line from
                                       # 'randomJokes.txt' was converted to a 1D array item.

for i in f1:                           # Now that each joke + punchline are individual items,
    setup.append(i[0] + "?")           # I made them separate 1D lists + I added a question mark for every joke item // since split() got rid of them in line 11.
    punchline.append(i[1])

for j, k in enumerate(punchline):      # 'enumerate()' is used for iterable items, to replace every '/n' with nothing
    punchline[j] = k.replace(char, '') # This is purely cosmetic.

# Functions
def entrycheck():
    global decider                     # 'decider' is a global variable so it'll reveal the correct punchline of a joke
                                       # with the same generated index number of the joke set line
    g = len(setup)                      
    decider = random.randint(0, g)
    
    userprompt = check.get()           # This gets the string input from the entrybox
    punchline2.config(text = " ")      # Everytime the 'ENTER' button is pressed, the jokes will reset
    setline.config(text = " ")
    
    if userprompt == "Alexa tell me a joke":
        subtitle3 = Label(jokes, bg = "#f2f540", fg = "gray", text = "Press the 'p' to reveal the punchline.", font = ("Comic Sans MS", 13))
        subtitle3.place(relx = 0.5, rely = 0.85, anchor = CENTER)
        setline.config(text = setup[decider])
        jokes.bind("p", puncher)             # 'bind()' essentially gets any keyboard/key input from the user and then executes a function (in the given arguement)

    else:
        subtitle.config(text = "Please enter 'Alexa tell me a joke' again.")

def puncher(event = None):                       # event = None doesn't exactly do anything but allow for some flexibility with the code
    global decider
    punchline2.config(text = punchline[decider]) # This reveals the punchline when the p key is pressed
    
# Main Program
jokes = tk.Tk()
check = tk.StringVar(jokes)                      # The check variable is what is used to store the user's prompt
jokes.title("Free Joke Generator...")
jokes.geometry("600x670")
jokes.config(bg = "#f2f540")

title = Label(jokes, bg = "#f2f540", text = "Random Joke Generator", font = ("Comic Sans MS", 25))
title.place(relx = 0.5, rely = 0.1, anchor = CENTER)

subtitle = Label(jokes, bg = "#f2f540", text = "Enter: 'Alexa tell me a joke' ", font = ("Comic Sans MS", 13))
subtitle.place(relx = 0.5, rely = 0.25, anchor = CENTER)

prompt = Entry(jokes, textvariable = check, width = 30, font = ("Comic Sans MS", 15), bd=3)
prompt.place(relx = 0.5, rely = 0.4, anchor = CENTER)

enter = tk.Button(jokes, 
                text = "ENTER", 
                fg = "White", 
                bg = "#44703f", font = ("Comic Sans MS", 15), height = 1, width = 10, command = lambda: entrycheck())
enter.place(relx = 0.5, rely = 0.55, anchor = CENTER)

setline = Label(jokes, bg = "#f2f540", fg = "#004763", text = "", font = ("Comic Sans MS", 14))
setline.place(relx = 0.5, rely = 0.675, anchor = CENTER)

punchline2 = Label(jokes, bg = "#f2f540", fg = "#c26f04", text = "", font = ("Comic Sans MS", 18))
punchline2.place(relx = 0.5, rely = 0.75, anchor = CENTER)

jokes.mainloop()