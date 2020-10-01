from entity.board import Board
from entity.cell import Cell

board = Board()
cells = []

for i in range(9):
    row = []
    for j in range(9):
        row.insert(Cell(None, [i, j]))
    cells.insert(row)

board.cells = cells