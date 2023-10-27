from tkinter import *
import random
root = Tk()

root.title('Крестики нолики')
root.geometry('350x350')

games = Canvas(root, width=300, height=300, bg="red")
#games.pack()
games.pack(anchor=CENTER, expand=1)
#games.place(x=25, y=25)

condition = [None] * 9
win = None
combination = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7)]
for i in range(0, 9):
    x = i // 3 * 100
    y = i % 3 * 100
    games.create_rectangle(x, y, x+100, y + 100,
                           width=3,
                           outline="#A5A5A5",
                           fill="#CCCCCC",
                           activefill="#FFFAFA")


def add_x(column, row):
    x = 10 + 100 * column
    y = 10 + 100 * row
    games.create_line(x, y, x + 80, y + 80, width=7, fill='red')
    games.create_line(x, y+80, x+80, y, width=7, fill='#0000FF')


def add_0(column, row):
    x = 10 + 100 * column
    #dsff
    y = 10 + 100 * row
    games.create_oval(x, y, x + 80, y + 80, width=7, fill='red')
    #games.create_line(x, y+80, x+80, y, width=7, fill='#0000FF')

def click(event):
    column = event.x // 100
    row = event.y // 100
    index = column + row * 3
    if condition[index] is None:
        condition[index] = 'x'
        add_x(column, row)
    bot_move()
    print(condition)


def bot_move():
    empty_indexes = []
    for index, el in enumerate(condition):
        if el is None:
            empty_indexes.append(index)
    if empty_indexes:
        index = random.choice(empty_indexes)
        condition[index] = 'o'
        column = index % 3
        row = index // 3
        add_0(column, row)

games.bind('<Button-1>', click)



root.mainloop()
