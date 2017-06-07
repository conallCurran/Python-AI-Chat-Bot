import Tkinter as tk
from Tkinter import *

from PIL import ImageTk, Image
import random

root = Tk()
root.geometry("1500x1000")
root.overrideredirect(1)
root.attributes('-alpha', 1.0)

image = Image.open("images/giphy.gif")
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.image = photo
label.pack()

T = Text(root, height=2, width=30)
T.pack()

text = tk.Text()
text.pack()


def getdata():

    greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!', 'hey']
    random_greeting = random.choice(greetings)

    question = ['How are you?', 'How are you doing?', 'What are you up to', 'Hows it hanging', 'hows the form']
    responses = ['Okay', 'Im getting on the best what about you?']
    random_response = random.choice(responses)

    sport = ['Do you play Sport', 'Do you like Sport']
    responsesSport = ['Yes I love Sport', 'No I hate Sport!!!']
    random_response_Sport = random.choice(responsesSport)

    while True:
        userInput = T.get("1.0", 'end-1c')
        if userInput in greetings:
            print random_greeting
            text.insert(tk.END, random_greeting + '\n')
        elif userInput in question:
            print random_response
            text.insert(tk.END, random_response + '\n')
        elif userInput in sport:
            print random_response_Sport
            text.insert(tk.END, random_response_Sport + '\n')
        else:
            print ('I did not understand what you said')
            text.insert(tk.END, 'Sorry my responses are limited! You must ask the right questions.')
        return

button1 = Button(text = "Ask Question", bg = "Green", command= getdata)
button1.place(x= 880, y = 410)




root.mainloop()


