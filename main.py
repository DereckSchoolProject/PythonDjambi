from entity.board import Board
from entity.cell import Cell
from tkinter import *

cells = []
for i in range(9):
    row = []
    for j in range(9):
        pos = [i, j]
        row.append(Cell(peons=None, position=pos))
    cells.append(row)
board = Board(cells)
board.init_place()

if __name__ == '__main__':
    fenetre = Tk()
    fenetre.title('Djambi')
    for rowCells in cells:
        for row in rowCells:
            if row.peons != None:
                photo = PhotoImage(file=row.peons.icon)
                btn = Button(fenetre, bg=row.peons.color, image=photo)
                btn.image = photo
                btn.grid(row=row.get_pos_x(), column=row.get_pos_y())
            else:
                photo = PhotoImage(file=r'./icons/blank.png')
                btn = Button(fenetre, bg='white', image=photo)
                btn.image = photo
                btn.grid(row=row.get_pos_x(), column=row.get_pos_y())
    fenetre.mainloop()