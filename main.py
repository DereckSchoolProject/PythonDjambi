from entity.board import Board
from entity.cell import Cell
from entity.peons import *
from tkinter import *

cells = []

for i in range(9):
    row = [Cell]
    for j in range(9):
        pos = [i, j]
        row.append(Cell(peons=None, position=pos))
    cells.append(row)
board = Board(cells)

if __name__ == '__main__':
    fenetre = Tk()
    fenetre.title('Djambi')
    for x in cells:
        for y in x:
            photo = PhotoImage(file="./icons/chief.png")
            btn = Button(fenetre, bg='blue', image=photo)
            btn.image = photo
            btn.grid(row= y.getPosX(), column= y.getPosX())
    fenetre.mainloop()