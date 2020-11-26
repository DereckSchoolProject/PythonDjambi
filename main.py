from entity.board import Board
from entity.cell import Cell
from tkinter import *

TITLE_NAME = 'Djambi'
BITMAP_ICON = './chief.ico'
ICON_BLANK = './icons/blank.png'
COLOR_WHITE = 'white'
COLOR_BLACK = 'black'
UNSELECTED_RELIEF = 'ridge'
SELECTED_RELIEF = 'sunken'


def click_cell(x: int, y: int):
    """ Actions on click on cell on the board. """
    if (board.cells[x][y].peons is not None and board.cells[x][y].peons.is_alive and board.dead_peon is None) or \
            (board.selected_cell is not None and board.cells[x][y].peons is None) or \
            (board.dead_peon is not None and board.cells[x][y].peons is None):
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
    """ Load cells on the board. """
    x = cell.get_pos_x()
    y = cell.get_pos_y()
    photo = PhotoImage(file=ICON_BLANK)
    color = COLOR_WHITE
    relief = UNSELECTED_RELIEF

    if cell.peons is not None:
        if cell.peons.is_alive:
            photo = PhotoImage(file=cell.peons.icon)
            color = cell.peons.color
        else:
            color = COLOR_BLACK

    if cell == board.selected_cell:
        relief = SELECTED_RELIEF

    btn = Button(window, bg=color, image=photo, borderwidth=5, relief=relief,
                 command=lambda x=x, y=y: click_cell(x, y))
    btn.image = photo
    btn.grid(row=x, column=y)


if __name__ == '__main__':
    """ Initialize the board. """
    cells = []
    for i in range(9):
        row = []
        for j in range(9):
            pos = [i, j]
            row.append(Cell(peons=None, position=pos))
        cells.append(row)
    board = Board(cells)
    board.init_place()

    """ Create UI windows. """
    window = Tk()
    window.resizable(0, 0)
    window.title(TITLE_NAME)
    window.iconbitmap(BITMAP_ICON)
    for rowCells in board.cells:
        for row in rowCells:
            load_cell(row)
    window.mainloop()
