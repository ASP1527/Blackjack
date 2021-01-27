#imports
from dealer import *
from player import *
from random import *
import tkinter as tk
from tkinter import *

#subroutine variables

deck = []

#subroutines

def setDeck():
    global deck
    cardNumber = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    cardName = ['Hearts','Spades','Clubs','Diamonds']
    for i in cardName:
        for j in cardNumber:
            deck.append(i + " " + j)
    shuffle(deck)


#main program

setDeck()
#print(deck)
p = player([], 0)
computer = dealer([], 0)

root = Tk()
root.title("Blackjack")
root.geometry("1000x1000")
root.configure(bg="#523002")
root.resizable()

frame = tk.Frame(root, bg="#12553c")
frame.place(relwidth=0.9, relheight = 0.9, relx=0.05, rely=0.05)

hit = Button(root, text="Hit Me", padx=29, pady=5, bg="blue", fg="white", command=p.hit(deck))
hit.pack()



root.mainloop()