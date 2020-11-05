from entity.board import Board
from entity.cell import Cell
from tkinter import *


def click_cell(x: int, y: int):
    last_x = -1
    last_y = -1
    if board.selected_cell is not None:
        last_x = board.selected_cell.get_pos_x()
        last_y = board.selected_cell.get_pos_y()
    board.select_peons(x, y)

    if last_x != -1 and last_y != -1:
        load_cell(board.cells[last_x][last_y])
    load_cell(board.cells[x][y])


def load_cell(cell: Cell):
    x = cell.get_pos_x()
    y = cell.get_pos_y()
    photo = PhotoImage(file=r'./icons/blank.png')
    color = 'white'

    if cell.peons is not None:
        photo = PhotoImage(file=cell.peons.icon)
        color = cell.peons.color

    btn = Button(fenetre, bg=color, image=photo)
    btn.image = photo
    btn.bind('<Button-1>', click_cell(x, y))
    btn.grid(row=x, column=y)


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
    for rowCells in board.cells:
        for row in rowCells:
            load_cell(row)
    fenetre.mainloop()
