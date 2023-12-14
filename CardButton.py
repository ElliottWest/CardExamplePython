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

def makeButton():
    button = Button(master=gameButtons,
    width=50,
    height=68,
    bg="black",
    fg="white",
    command=lambda: handleClick()
    )
    return button


def buildDeck():
    for v in range(len(values)):
        for s in range(len(suits)):
            buttonPath = "images/card" + suits[s] + values[v] + ".png"
            cardImagesList.append(buttonPath)

        
def handleClick():
    print()


buildDeck()


deal = 5
for c in range(deal):
    b = makeButton()
    #we have to store the buttons in an array because they are objects
    dealt.append(b)
    buttonImage = PhotoImage(file = cardImagesList[c])
    #we have to store the images in an array because they are objects
    imageObjects.append(buttonImage)
    #we get the last button created and place the last image created on it
    b.config(image = buttonImage)
    b.pack()
    

gameButtons.pack(side = LEFT, fill=BOTH, expand=True)
window.mainloop()