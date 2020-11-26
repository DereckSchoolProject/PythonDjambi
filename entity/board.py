from entity.cell import Cell
from entity.peons import *


class Board:
    """ Representation of the board. """

    COLOR_YELLOW_TEAM = 'yellow'
    COLOR_RED_TEAM = 'red'
    COLOR_BLUE_TEAM = 'blue'
    COLOR_GREEN_TEAM = 'green'

    def __init__(self, cells: [Cell]):
        """ Initialize methode. """
        self._cells = cells
        self._teams = []
        self._selected_cell = None
        self._dead_peon = None

    def get_selected_cell(self):
        """ Getter of selected_cell. """
        return self._selected_cell

    def set_selected_cell(self, selected_cell: Cell):
        """ Setter of selected_cell. """
        self._selected_cell = selected_cell

    def get_dead_peon(self):
        """ Getter of dead_peon. """
        return self._dead_peon

    def set_dead_peon(self, dead_peon: Peons):
        """ Setter of dead_peon. """
        self._dead_peon = dead_peon

    def get_cells(self):
        """ Getter of cells. """
        return self._cells

    def set_cells(self, cells: []):
        """ Setter of cells. """
        self._cells = cells

    def move(self, x: int, y: int):
        """ Move a peon on the board. """
        if self._selected_cell is not None:
            cell = self._cells[x][y]
            if cell.peons is not None:
                self._dead_peon = cell.peons
                self._dead_peon.is_alive = False
            cell.peons = self._selected_cell.peons
            self._selected_cell.peons = None

    def move_death(self, x: int, y: int):
        """ Move a dead peon on the board. """
        cell = self._cells[x][y]
        cell.peons = self._dead_peon

    def select_peons(self, x: int, y: int):
        """ Do an actions with the peons selected.
        if dead peons was selected, we can place it on blank cell.
        if peons was selected, we can place it on the board.
        if selected peon was selected, we deselect them."""
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
        """ Initialize all peons on the board. """
        self.init_yellow_team()
        self.init_red_team()
        self.init_blue_team()
        self.init_green_team()

    def init_yellow_team(self):
        """ Initialize all peons of the yellow team. """
        self._cells[0][0].peons = Chief(self.COLOR_YELLOW_TEAM)
        self._cells[0][1].peons = Assasins(self.COLOR_YELLOW_TEAM)
        self._cells[1][0].peons = Reporter(self.COLOR_YELLOW_TEAM)
        self._cells[1][1].peons = Diplomat(self.COLOR_YELLOW_TEAM)
        self._cells[2][2].peons = Necromobile(self.COLOR_YELLOW_TEAM)
        self._cells[0][2].peons = Militant(self.COLOR_YELLOW_TEAM)
        self._cells[1][2].peons = Militant(self.COLOR_YELLOW_TEAM)
        self._cells[2][0].peons = Militant(self.COLOR_YELLOW_TEAM)
        self._cells[2][1].peons = Militant(self.COLOR_YELLOW_TEAM)

    def init_red_team(self):
        """ Initialize all peons of the red team. """
        self._cells[8][8].peons = Chief(self.COLOR_RED_TEAM)
        self._cells[8][7].peons = Assasins(self.COLOR_RED_TEAM)
        self._cells[7][8].peons = Reporter(self.COLOR_RED_TEAM)
        self._cells[7][7].peons = Diplomat(self.COLOR_RED_TEAM)
        self._cells[6][6].peons = Necromobile(self.COLOR_RED_TEAM)
        self._cells[8][6].peons = Militant(self.COLOR_RED_TEAM)
        self._cells[7][6].peons = Militant(self.COLOR_RED_TEAM)
        self._cells[6][8].peons = Militant(self.COLOR_RED_TEAM)
        self._cells[6][7].peons = Militant(self.COLOR_RED_TEAM)

    def init_blue_team(self):
        """ Initialize all peons of the blue team. """
        self._cells[8][0].peons = Chief(self.COLOR_BLUE_TEAM)
        self._cells[8][1].peons = Assasins(self.COLOR_BLUE_TEAM)
        self._cells[7][0].peons = Reporter(self.COLOR_BLUE_TEAM)
        self._cells[7][1].peons = Diplomat(self.COLOR_BLUE_TEAM)
        self._cells[6][2].peons = Necromobile(self.COLOR_BLUE_TEAM)
        self._cells[8][2].peons = Militant(self.COLOR_BLUE_TEAM)
        self._cells[7][2].peons = Militant(self.COLOR_BLUE_TEAM)
        self._cells[6][0].peons = Militant(self.COLOR_BLUE_TEAM)
        self._cells[6][1].peons = Militant(self.COLOR_BLUE_TEAM)

    def init_green_team(self):
        """ Initialize all peons of the green team. """
        self._cells[0][8].peons = Chief(self.COLOR_GREEN_TEAM)
        self._cells[0][7].peons = Assasins(self.COLOR_GREEN_TEAM)
        self._cells[1][8].peons = Reporter(self.COLOR_GREEN_TEAM)
        self._cells[1][7].peons = Diplomat(self.COLOR_GREEN_TEAM)
        self._cells[2][6].peons = Necromobile(self.COLOR_GREEN_TEAM)
        self._cells[0][6].peons = Militant(self.COLOR_GREEN_TEAM)
        self._cells[1][6].peons = Militant(self.COLOR_GREEN_TEAM)
        self._cells[2][8].peons = Militant(self.COLOR_GREEN_TEAM)
        self._cells[2][7].peons = Militant(self.COLOR_GREEN_TEAM)

    selected_cell = property(get_selected_cell, set_selected_cell)
    dead_peon = property(get_dead_peon, set_dead_peon)
    cells = property(get_cells, set_cells)
