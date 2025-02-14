from tkinter import *
from time import sleep

toggled = False

def seizure(mode):
    global toggled
    if button["text"] == "Start Seizure?":
        button["text"] = "Stop?"
        toggled = True
    else:
        button["text"] = "Start Seizure?"
        toggled = False
        window["bg"] = "#090909"
    
    if mode == "rainbow" and toggled:
        colors = ["red", "dark red", "orange",
                       "#E99B0F", "yellow",
                       "#F0DC82", "light green",
                       "green", "light blue", "blue",
                       "purple", "pink"]
        while toggled == True:
            for j in range(len(colors)):
                sleep(0.05)
                window["bg"] = colors[j]
                window.update()
        window["bg"] = "#090909"
    
    elif mode == "wobniar" and toggled:
        colors = ["red", "dark red", "orange",
                       "#E99B0F", "yellow",
                       "#F0DC82", "light green",
                       "green", "light blue", "blue",
                       "purple", "pink"]
        while toggled == True:
            for j in range(len(colors),0,-1):
                sleep(0.05)
                window["bg"] = colors[j-1]
                window.update()
        window["bg"] = "#090909"
    elif mode == "random" and toggled:
        colors = ["red", "dark red", "light grey",
                       "#E99B0F", "yellow",
                       "#F0DC82", "brown",
                       "black", "light blue", "blue",
                       "purple", "pink", "light yellow",
                       "maroon", "magenta", "lime",
                       "light green", "white", "green",
                       "grey", "turquoise", "dark green",
                       "orange", "hot pink"]
        while toggled == True:
            for j in range(len(colors),0,-1):
                sleep(0.05)
                window["bg"] = colors[j-1]
                window.update()
        window["bg"] = "#090909"
    
    else:
        if button["text"] == "Stop?":
            button["text"] = "Start Seizure?"
            toggled = False
#


window = Tk()
window["bg"] = "#090909"

button = Button(window,
               text="Start Seizure?",
               font=("consolas",10),
               bg="#101010",
               fg="light grey",
               activebackground="red",
               activeforeground="sky blue",
               command=lambda mode = "random":
                   seizure(mode))
button.place(relx=0.5,rely=0.8,anchor=CENTER)

window.mainloop()