# Testing file: crosswords/1976/01/01.json

import json
from tkinter import *
from functools import partial
import random
import os


def addtoDic (words, clues):
    tempDic = {}
    for i in range(len(words)):
        temp = tuple(words[i])
        clue = clues[i][clues[i].find(' ') + 1:] # removes the clue number from the front of the clue
        tempDic[temp] = clue
    return tempDic


def getCrossword():
    year = random.choice(os.listdir(os.getcwd() + "\Crosswords"))
    year = os.path.basename(year)
    print(year)
    month = random.choice(os.listdir(os.getcwd() + "\Crosswords\\" + year))
    month = os.path.basename(month)
    print(month)
    day = random.choice(os.listdir(os.getcwd() + "\Crosswords\\" + year + "\\" + month))
    day = os.path.basename(day)
    print(day)
    return os.getcwd() + "\\Crosswords\\" + year + "\\" + month + "\\" + day


def formatClues(acrossCluesList, downCluesList):
    # aSelector = Button(text='Across', command=Direction.setDirectionAcross)
    # aSelector.pack()

    acrossColumn = 'Across:\n'
    for clue in acrossCluesList:
        acrossColumn += clue + '\n'

    # dSelector = Button(text='Down', command=Direction.setDirectionDown)
    # dSelector.pack()

    downColumn = 'Down:\n'
    for clue in downCluesList:
        downColumn += clue + '\n'
    return acrossColumn, downColumn


def windowMaker(length, width, grid, gridNums):
    def correctText(currX, currY, *args):
        value = varList[currX][currY].get()

        if len(value) > 1: value = value[len(value) - 1]
        value = value.upper()

        varList[currX][currY].set(value)
        dir = True
        if dir:
            if currY < length - 1:
                count = 1
                while currY + count < length and varList[currX][currY + count].get() == ".":
                    count += 1
                if currY + count < length - 1:
                    textBoxes[currX][currY + count].focus()
                textBoxes[currX][currY + 1].focus()
            currY += 1
            if currY >= length:
                currY = 0
                count = 0
                while currY < length and varList[currX][currY + count].get() == ".":
                    count += 1
                currX += 1
                textBoxes[currX][currY + count].focus()
        else:
            if currX < width - 1:
                count = 1
                while currX + count < width and varList[currX + count][currY].get() == ".":
                    print("pepe")
                    count += 1
                if currX < width - 1:
                    textBoxes[currX + count][currY].focus()
                textBoxes[currX + 1][currY].focus()
            currX += 1
            if currX >= width:
                print(currX, currY, width)
                currX = 0
                currY += 1
                textBoxes[currX][currY].focus()

    def compareAnswer(*args):
        userInputs = []
        for stuff in varList:
            for thing in stuff:
                userInputs.append(thing.get())
        count = 0
        for x in range(0, len(textBoxes)):
            for y in range(0, len(textBoxes[x])):
                if userInputs[count] == grid[count]:
                    userInputs[count] = "."
                    textBoxes[x][y].configure(state="disabled")
                    # print(userInputs[count], "is correct")
                elif userInputs[count] == "":
                    textBoxes[x][y].configure(fg="black")
                else:
                    textBoxes[x][y].configure(fg="red")
                count += 1


    '''def getCrossword():
        year = random.choice(os.listdir(os.getcwd() + "\Crosswords"))
        year = os.path.basename(year)
        print(year)
        month = random.choice(os.listdir(os.getcwd() + "\Crosswords\\" + year))
        month = os.path.basename(month)
        print(month)
        day = random.choice(os.listdir(os.getcwd() + "\Crosswords\\" + year + "\\" + month))
        day = os.path.basename(day)
        print(day)
        return os.getcwd() + "\\Crosswords\\" + year + "\\" + month + "\\" + day'''



    root = Tk()
    root.title("Crossword Simulator 2020")
    root.minsize(1500, 950)

    mycolor = '#%02x%02x%02x' % (255, 255, 255)

    c = Canvas(bg=mycolor, width='512', height='512')
    c.pack(side='top', fill='both', expand='1')

    rects = [[None for x in range(width + 1)] for y in range(length + 1)]
    handles = [[None for x in range(width + 1)] for y in range(length + 1)]
    rsize = 512 / 10
    guidesize = 512 / 0.665

    (xr, yr) = (1 * rsize, 1 * rsize)
    rects[0][0] = c.create_rectangle(xr, yr, xr + guidesize,
                                     yr + guidesize, width=3)

    textBoxes = []
    varList = []

    count = 0
    for y in range(1, length + 1):
        boxRow = []
        varRow =[]

        for x in range(1, width + 1):
            var = StringVar()

            (xr, yr) = (x * rsize, y * rsize)
            r = c.create_rectangle(xr, yr, xr + rsize, yr + rsize)

            if grid[count] == ".":
                eFrame = Frame(root, width=25, height=25, background="black")
                eFrame.pack()
                c.create_rectangle(xr, yr, xr + rsize, yr + rsize, fill="black")
                e = Entry(eFrame, textvariable=var)
                var.set('.')
            else:
                eFrame = Frame(root, width=30, height=25)
                eFrame.pack()
                e = Entry(eFrame, font=("Comic Sans MS", 20), relief="flat", highlightcolor="white", justify="center",
                          textvariable=var)
                # adding each entry to a list, so they can be accessed later (for checking purposes)

                e.place(x=0, y=0, height=25, width=30)

            boxRow.append(e)

            t = c.create_window(xr + rsize / 2 + 5, yr + rsize / 2 + 5, window=eFrame)
            handles[y][x] = (r, t)

            varRow.append(var)

            if gridNums[count] != 0:
                c.create_text(xr + 10, yr + 10, fill="black", font=("Comic Sans MS", 10), text=gridNums[count])
            count += 1

        textBoxes.append(boxRow)
        varList.append(varRow)

    for y in range(0, length):
        for x in range(0, width):
            varList[x][y].trace('w', partial(correctText, x, y))

    root.canvas = c
    checkButton = Button(text="Check Puzzle", command=compareAnswer)
    checkButton.config(height=3, width=20)
    checkButton.pack(side=LEFT, padx=60, pady=20)

    displayClues(acrossString, downString, c)

    root.mainloop()


def displayClues(acrossString, downString, canvas):
    c = canvas
    c.create_text(850, 60, fill="black", font=("Comic Sans MS", 15), text=acrossString, anchor='nw')
    c.create_text(1050, 60, fill="black", font=("Comic Sans MS", 15), text=downString, anchor='nw')


# Begin main
file = open(getCrossword())
# direct = Direction()

jsonDta = json.load(file)

columns = jsonDta['size']['cols']
rows = jsonDta['size']['rows']
author = jsonDta['author']
editor = jsonDta['editor']
title = jsonDta['title']

acrossWords = jsonDta['answers']['across']
acrossClues = jsonDta['clues']['across']
downWords = jsonDta['answers']['down']
downClues = jsonDta['clues']['down']

allWords = acrossWords + downWords
allClues = acrossClues + downClues

grid = jsonDta['grid']
gridNums = jsonDta['gridnums']

acrossString, downString = formatClues(acrossClues, downClues)

windowMaker(rows, columns, grid, gridNums)
