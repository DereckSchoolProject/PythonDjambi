from entity.cell import Cell
from entity.peons import *


class Board:
    ''' représentation of the board '''

    def __init__(self, cells: [Cell]):
        self._cells = cells
        self._teams = []
        self._selected_cell = None
        self._dead_peon = None

    def get_selected_cell(self):
        return self._selected_cell

    def set_selected_cell(self, selected_cell: Cell):
        self._selected_cell = selected_cell

    def get_dead_peon(self):
        return self._dead_peon

    def set_dead_peon(self, dead_peon: Peons):
        self._dead_peon = dead_peon

    def get_cells(self):
        return self._cells

    def set_cells(self, cells: []):
        self._cells = cells

    def move(self, x: int, y: int):
        if self._selected_cell is not None:
            cell = self._cells[x][y]
            if cell.peons is not None:
                self._dead_peon = cell.peons
                self._dead_peon.is_alive = False
            cell.peons = self._selected_cell.peons
            self._selected_cell.peons = None

    def move_death(self, x: int, y: int):
        cell = self._cells[x][y]
        cell.peons = self._dead_peon

    def select_peons(self, x: int, y: int):
        cell = self._cells[x][y]

        if self._selected_cell != cell:
            if self._selected_cell is None:
                if self._dead_peon is None:
                    self._selected_cell = cell
                else:
                    self.move_death(x, y)
                    self._dead_peon = None
                    self._selected_cell = None
            else:
                if self._dead_peon is None:
                    self.move(x, y)
                    self._selected_cell = None
        else:
            self._selected_cell = None

    def init_place(self):
        self.init_yellow_team()
        self.init_red_team()
        self.init_blue_team()
        self.init_green_team()

    def init_yellow_team(self):
        self._cells[0][0].peons = Chief('yellow')
        self._cells[0][1].peons = Assasins('yellow')
        self._cells[1][0].peons = Reporter('yellow')
        self._cells[1][1].peons = Diplomate('yellow')
        self._cells[2][2].peons = Necromobile('yellow')
        self._cells[0][2].peons = Militant('yellow')
        self._cells[1][2].peons = Militant('yellow')
        self._cells[2][0].peons = Militant('yellow')
        self._cells[2][1].peons = Militant('yellow')

    def init_red_team(self):
        self._cells[8][8].peons = Chief('red')
        self._cells[8][7].peons = Assasins('red')
        self._cells[7][8].peons = Reporter('red')
        self._cells[7][7].peons = Diplomate('red')
        self._cells[6][6].peons = Necromobile('red')
        self._cells[8][6].peons = Militant('red')
        self._cells[7][6].peons = Militant('red')
        self._cells[6][8].peons = Militant('red')
        self._cells[6][7].peons = Militant('red')

    def init_blue_team(self):
        self._cells[8][0].peons = Chief('blue')
        self._cells[8][1].peons = Assasins('blue')
        self._cells[7][0].peons = Reporter('blue')
        self._cells[7][1].peons = Diplomate('blue')
        self._cells[6][2].peons = Necromobile('blue')
        self._cells[8][2].peons = Militant('blue')
        self._cells[7][2].peons = Militant('blue')
        self._cells[6][0].peons = Militant('blue')
        self._cells[6][1].peons = Militant('blue')

    def init_green_team(self):
        self._cells[0][8].peons = Chief('Green')
        self._cells[0][7].peons = Assasins('Green')
        self._cells[1][8].peons = Reporter('Green')
        self._cells[1][7].peons = Diplomate('Green')
        self._cells[2][6].peons = Necromobile('Green')
        self._cells[0][6].peons = Militant('Green')
        self._cells[1][6].peons = Militant('Green')
        self._cells[2][8].peons = Militant('Green')
        self._cells[2][7].peons = Militant('Green')

    selected_cell = property(get_selected_cell, set_selected_cell)
    dead_peon = property(get_dead_peon, set_dead_peon)
    cells = property(get_cells, set_cells)
