from tkinter import *

window = Tk()
window.title("Card Button Example")
window.geometry("+0+0")

#creates raised frames
controls = Frame(window, 
    relief = RAISED, 
    borderwidth = 5)
gameButtons = Frame(window,
    relief = RAISED,
    borderwidth = 5)

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
values = ["2","3","4","5","6","7","8","9","10","A","J","Q","K"]

dealt = []
imageObjects = []
cardImagesList = []#this is a list of image paths

def makeButton(i):
    button = Button(master=gameButtons,
    width=50,
    height=68,
    bg="black",
    fg="white",
    command=lambda: handleClick(i)
    )
    return button


def buildDeck():
    for v in range(len(values)):
        for s in range(len(suits)):
            buttonPath = "images/card" + suits[s] + values[v] + ".png"
            cardImagesList.append(buttonPath)

        
def handleClick(i):
    print(i)


buildDeck()


deal = 10
r = 0
c = 0
count = 0
for card in range(deal):
    b = makeButton(cardImagesList[card])
    #we have to store the buttons in an array because they are objects
    dealt.append(b)
    buttonImage = PhotoImage(file = cardImagesList[card])
    #we have to store the images in an array because they are objects
    imageObjects.append(buttonImage)
    b.config(image = buttonImage)
    if(count % 10 == 0):
        c = 0
        r += 1
    count += 1
    c += 1
    b.grid(row = r, column = c)


gameButtons.pack(side = LEFT, fill=BOTH, expand=True)
window.mainloop()