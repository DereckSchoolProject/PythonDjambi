from entity.peons import Peons

class Cell:
    ''' Représentation of the cell in the board '''
    def __init__(self, peons:Peons, position:tuple):
        self._peons = peons
        self._position = position

    def getPeons(self):
        return self._peons

    def getPosX(self):
        return self._position.index(0)

    def getPosY(self):
        return self._position.index(1)