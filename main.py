from entity.board import Board
from entity.cell import Cell
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
    for rowCells in cells:
        for row in rowCells:
            photo = PhotoImage(file="./icons/chief.png")
            btn = Button(fenetre, bg='blue', image=photo)
            btn.image = photo
            btn.grid(row=row.get_pos_x, column=row.get_pos_y())
    fenetre.mainloop()