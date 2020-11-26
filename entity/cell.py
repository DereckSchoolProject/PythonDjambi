from entity.peons import Peons


class Cell:
    """ Representation of the cell in the board. """

    def __init__(self, peons: Peons, position: list):
        """ Initialize methode. """
        self._peons = peons
        self._position = position

    def get_peons(self):
        """ Getter of peons. """
        return self._peons

    def set_peons(self, peons: Peons):
        """ Setter of peons. """
        self._peons = peons

    def get_pos_x(self):
        """ Getter of position x on position attribute. """
        return self._position[0]

    def get_pos_y(self):
        """ Getter of position y on position attribute. """
        return self._position[1]

    peons = property(get_peons, set_peons)
