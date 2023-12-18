from tkinter import *
import random
import time
window = Tk()
window.title("button click")
frameForLabel = Frame(window)
frameForLabel.pack(side = "top")
frameForButton = Frame(window)
frameForButton.pack(side = "bottom")
sumValue = 0
stateForButton = [[False] * 10 for _ in range(10)]
timeRamaining = 60
timerLabel = Label(frameForLabel, text= "time remaining: 1:00")
timerLabel.grid(row=0, column=0)
hasWon = False
def hndleClick(i, j):
    global sumValue, hasWon
    stateForButton[i][j] = not stateForButton[i][j]
    if stateForButton[i][j]:
        sumValue += i * 10 + j + 1
        if random.randint(0,1):
            showImage(i, j)
    else:
        sumValue -= i * 10 + j + 1

    labelTotal.config(text="Current total: {}".format(sumValue))
    resetTimer()

def showImage(i, j):
    global hasWon
    img = PhotoImage(file="images/krampus.gif")
    img = img.subsample(2)
    label = Label(frameForButton, image=img, borderwidth=0)
    label.image = img
    label.grid(row=1, column = j)
    label.bind("<Button-1>", lambda event, i=i, j=j: checkWin())

    startTimer()

def startTimer():
    window.after(1000, updateTimer)

def updateTimer():
    global remainingTime
    remainingTime -= 1
    minutes = remainingTime // 60
    seconds = remainingTime % 60
    timerLabel.config(text="Time remaining: {:02d}:{:02d}".format(minutes,seconds))

    if remainingTime > 0:
        window.after(1000,updateTimer)
    else:
        checkWin()

def resetTimer():
    global remainingTime
    remainingTime = 60
    updateTimer()

def checkWin():
    global hasWon
    if not hasWon:
        labelTotal.config(text= "You provoked Krampus within the minute.")
        hasWon = True
    

for i in range(10):
    for j in range(10):
        button = Button(
            frameForButton,
            text="",
            width = 5,
            height = 2,
            bg= "white",
            borderwidth= 1,
            command=lambda i=i, j=j: hndleClick(i, j),
            relief=SUNKEN if stateForButton[i][j] else RAISED
        )
        button.grid(row=i, column=j,)

labelTotal = Label(frameForLabel, text="Current total: {}".format(sumValue))
labelTotal.grid(row=0, column=0)
window.mainloop()