from entity.peons import Peons

class Cell:
    ''' Représentation of the cell in the board '''
    def __init__(self, peons:Peons, position:tuple):
        self._peons = peons
        self._position = position
