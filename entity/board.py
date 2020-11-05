from entity.cell import Cell
from entity.teams import Teams
from entity.peons import *


class Board:
    ''' représentation of the board '''

    def __init__(self, cells: [Cell]):
        self.cells = cells
        self.teams = []

    def move(self):
        return True

    def init_place(self):
        self.init_yellow_team()
        self.init_red_team()
        self.init_blue_team()
        self.init_green_team()

    def init_yellow_team(self):
        self.cells[0][0].peons = Chief('yellow')
        self.cells[0][1].peons = Assasins('yellow')
        self.cells[1][0].peons = Reporter('yellow')
        self.cells[1][1].peons = Diplomate('yellow')
        self.cells[2][2].peons = Necromobile('yellow')
        self.cells[0][2].peons = Militant('yellow')
        self.cells[1][2].peons = Militant('yellow')
        self.cells[2][0].peons = Militant('yellow')
        self.cells[2][1].peons = Militant('yellow')

    def init_red_team(self):
        self.cells[8][8].peons = Chief('red')
        self.cells[8][7].peons = Assasins('red')
        self.cells[7][8].peons = Reporter('red')
        self.cells[7][7].peons = Diplomate('red')
        self.cells[6][6].peons = Necromobile('red')
        self.cells[8][6].peons = Militant('red')
        self.cells[7][6].peons = Militant('red')
        self.cells[6][8].peons = Militant('red')
        self.cells[6][7].peons = Militant('red')

    def init_blue_team(self):
        self.cells[8][0].peons = Chief('blue')
        self.cells[8][1].peons = Assasins('blue')
        self.cells[7][0].peons = Reporter('blue')
        self.cells[7][1].peons = Diplomate('blue')
        self.cells[6][2].peons = Necromobile('blue')
        self.cells[8][2].peons = Militant('blue')
        self.cells[7][2].peons = Militant('blue')
        self.cells[6][0].peons = Militant('blue')
        self.cells[6][1].peons = Militant('blue')

    def init_green_team(self):
        self.cells[0][8].peons = Chief('Green')
        self.cells[0][7].peons = Assasins('Green')
        self.cells[1][8].peons = Reporter('Green')
        self.cells[1][7].peons = Diplomate('Green')
        self.cells[2][6].peons = Necromobile('Green')
        self.cells[0][6].peons = Militant('Green')
        self.cells[1][6].peons = Militant('Green')
        self.cells[2][8].peons = Militant('Green')
        self.cells[2][7].peons = Militant('Green')
