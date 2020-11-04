from entity.board import Board
from entity.cell import Cell
from tkinter import *

cells = []

for i in range(9):
    row = [Cell]
    for j in range(9):
        pos = [i, j]
        c = Cell(peons=None, position=pos)
        row.append(c)
    cells.append(row)
board = Board(cells)

if __name__ == '__main__':
    fenetre = Tk()
    fenetre.title('Djambi')
    label = Label(fenetre, text='Bienvenue sur Djambi Python')
    label.pack()
    fenetre.mainloop()