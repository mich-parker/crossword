from tkinter import *
import tkinter.font as font

def compareAnswer():
    print("CHECKED")


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

    for y in range(1, 11):
        row = []
        for x in range(1, 11):
            row.append(".")
            (xr, yr) = (x * rsize, y * rsize)
            r = c.create_rectangle(xr, yr, xr + rsize, yr + rsize)

            eFrame = Frame(root, width=40, height=39)
            eFrame.pack()

            e = Entry(eFrame, font=("Comic Sans MS", 24))
            e.place(x=0, y=0, height=40, width=39)
            t = c.create_window(xr + rsize / 2, yr + rsize / 2, window=eFrame)
            handles[y][x] = (r, t)
        userInputs.append(row)

    root.canvas = c
    checkButton = Button(text="Check Puzzle", command=compareAnswer)
    checkButton.config(height=3, width=20)
    checkButton.pack(side=LEFT, padx=60, pady=20)

    root.mainloop()


windowMaker(5, 5, [], [])
