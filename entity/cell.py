from entity.peons import Peons

class Cell:
    ''' Représentation of the cell in the board '''
    def __init__(self, peons:Peons, position:tuple):
        self._peons = peons
        self._position = position

    def get_peons(self):
        return self._peons

    def get_pos_x(self):
        return self._position[0]

    def get_pos_y(self):
        return self._position[1]