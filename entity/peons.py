from abc import ABC
from entity.cell import Cell

class Peons(ABC):
    def __init__(self, color:str, cell:Cell):
        self._isAlive = True
        self._color = color
        self._cell:cell
        self._icon:str

    def availableMove(self):
        return True

    def afterMove(self):
        return True

class Chief(Peons):
    icon:str = "icons/chief.png"

    def availableMove(self):
        return True

    def afterMove(self):
        return True

class Assasins(Peons):
    icon:str = "icons/assassin.png"

    def availableMove(self):
        return True

    def afterMove(self):
        return True

class Militant(Peons):
    icon:str = "icons/militant.png"

    def availableMove(self):
        return True

    def afterMove(self):
        return True

class Reporter(Peons):
    icon:str = "icons/reporter.png"

    def availableMove(self):
        return True

    def afterMove(self):
        return True

class Diplomate(Peons):
    icon:str = "icons/diplomate.png"

    def availableMove(self):
        return True

    def afterMove(self):
        return True

class Necromobile(Peons):
    icon:str = "icons/necromobile.png"

    def availableMove(self):
        return True

    def afterMove(self):
        return True
