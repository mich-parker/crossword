# Testing file: crosswords/1976/01/01.json

import json
from tkinter import *
import tkinter.font as font


def addtoDic (words, clues):
    tempDic = {}
    for i in range(len(words)):
        temp = tuple(words[i])
        clue = clues[i][clues[i].find(' ') + 1:] # removes the clue number from the front of the clue
        tempDic[temp] = clue
    return tempDic


def formatClues(acrossCluesList, downCluesList):
    acrossColumn = 'Across:\n'
    for clue in acrossCluesList:
        acrossColumn += clue + '\n'
    downColumn = 'Down\n'
    for clue in downCluesList:
        downColumn += clue + '\n'
    return acrossColumn, downColumn


def compareAnswer(userAnswers, answers):
    for i in range(len(answers)):
        if userAnswers[i] != answers[i]:
            break # implement after merging with the gui


# def correctText(*args):




def windowMaker(length, width, grid, gridNums):
    root = Tk()
    root.title("Crossword Simulator 2020")
    root.minsize(1200, 800)

    # customFont = font.Font("Comic Sans MS", 18)

    mycolor = '#%02x%02x%02x' % (255, 255, 255)

    c = Canvas(bg=mycolor, width='512', height='512')
    c.pack(side='top', fill='both', expand='1')

    rects = [[None for x in range(20)] for y in range(20)]
    handles = [[None for x in range(20)] for y in range(20)]
    rsize = 512 / 8
    guidesize = 512 / 0.8

    (xr, yr) = (1 * rsize, 1 * rsize)
    rects[0][0] = c.create_rectangle(xr, yr, xr + guidesize,
                                     yr + guidesize, width=3)
    userInputs = []
    textBoxes = []

    for y in range(1, 11):
        row = []
        boxRow = []
        for x in range(1, 11):
            row.append(".")
            (xr, yr) = (x * rsize, y * rsize)
            r = c.create_rectangle(xr, yr, xr + rsize, yr + rsize)

            eFrame = Frame(root, width=40, height=39)
            eFrame.pack()

            e = Entry(eFrame, font=("Comic Sans MS", 24), relief="flat", highlightcolor="white")
            boxRow.append(e)
            e.place(x=0, y=0, height=40, width=39)
            t = c.create_window(xr + rsize / 2, yr + rsize / 2, window=eFrame)
            handles[y][x] = (r, t)
        textBoxes.append(boxRow)
        userInputs.append(row)

    root.canvas = c
    checkButton = Button(text="Check Puzzle", command=compareAnswer)
    checkButton.config(height=3, width=20)
    checkButton.pack(side=LEFT, padx=60, pady=20)

    root.mainloop()


# Begin main
file = open(input("Enter name of crossword file to open: "))

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

windowMaker(5, 5, grid, gridNums)