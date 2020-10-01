class Board:
    ''' représentation of the board '''
    def __init__(self, dim:tuple, cells:list):
        self.dim = dim
        self.cells = cells

    def move(self):
        return True