from entity.peons import Peons


class Cell:
    ''' Représentation of the cell in the board '''

    def __init__(self, peons: Peons, position: list):
        self._peons = peons
        self._position = position

    def get_peons(self):
        return self._peons

    def set_peons(self, peons: Peons):
        self._peons = peons

    def get_pos_x(self):
        return self._position[0]

    def get_pos_y(self):
        return self._position[1]

    peons = property(get_peons, set_peons)
