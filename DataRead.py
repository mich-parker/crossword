# Testing file: crosswords/1976/01/01.json

import json


def addtoDic (words, clues):
    for i in range(len(words)):
        temp = tuple(words[i])
        # print(temp)
        globalDic[temp] = clues[i]


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

globalDic = {}
print(globalDic)
print("this line is a break")
addtoDic(allWords, allClues)
print(globalDic)

