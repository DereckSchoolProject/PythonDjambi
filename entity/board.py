from entity.cell import Cell

class Board:
    ''' représentation of the board '''
    def __init__(self, cells:[Cell]):
        self.cells = cells

    def move(self):
        return True
