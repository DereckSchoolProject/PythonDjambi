from abc import ABC
from entity.cell import Cell

class Peons(ABC):
    ''' representation of peons '''
    def __init__(self, color:str, cell:Cell):
        self._is_alive = True
        self._color = color
        self._cell:cell
        self._icon:str

    def availableMove(self):
        return True

    def afterMove(self):
        return True

class Chief(Peons):
    ''' representation of chief peons '''
    icon:str = "icons/chief.png"

    def availableMove(self):
        return True

    def afterMove(self):
        return True

class Assasins(Peons):
    ''' representation of assasins peons '''
    icon:str = "icons/assassin.png"

    def availableMove(self):
        return True

    def afterMove(self):
        return True

class Militant(Peons):
    ''' representation of militant peons '''
    icon:str = "icons/militant.png"

    def availableMove(self):
        return True

    def afterMove(self):
        return True

class Reporter(Peons):
    ''' representation of reporter peons '''
    icon:str = "icons/reporter.png"

    def availableMove(self):
        return True

    def afterMove(self):
        return True

class Diplomate(Peons):
    ''' representation of diplomate peons '''
    icon:str = "icons/diplomate.png"

    def availableMove(self):
        return True

    def afterMove(self):
        return True

class Necromobile(Peons):
    ''' representation of necromobile peons '''
    icon:str = "icons/necromobile.png"

    def availableMove(self):
        return True

    def afterMove(self):
        return True
