from abc import ABC


class Peons(ABC):
    ''' representation of peons '''

    def __init__(self, color: str):
        self._is_alive = True
        self._color = color
        self._icon: str

    def availableMove(self):
        return True

    def afterMove(self):
        return True

    def get_icon(self):
        return self._icon

    def get_color(self):
        return self._color

    def set_color(self, color: str):
        self._color = color

    icon = property(get_icon)
    color = property(get_color, set_color)


class Chief(Peons):
    ''' representation of chief peons '''
    _icon: str = "icons/chief.png"

    def availableMove(self):
        return True

    def afterMove(self):
        return True


class Assasins(Peons):
    ''' representation of assasins peons '''
    _icon: str = "icons/assassin.png"

    def availableMove(self):
        return True

    def afterMove(self):
        return True


class Militant(Peons):
    ''' representation of militant peons '''
    _icon: str = "icons/militant.png"

    def availableMove(self):
        return True

    def afterMove(self):
        return True


class Reporter(Peons):
    ''' representation of reporter peons '''
    _icon: str = "icons/reporter.png"

    def availableMove(self):
        return True

    def afterMove(self):
        return True


class Diplomate(Peons):
    ''' representation of diplomate peons '''
    _icon: str = "icons/diplomate.png"

    def availableMove(self):
        return True

    def afterMove(self):
        return True


class Necromobile(Peons):
    ''' representation of necromobile peons '''
    _icon: str = "icons/necromobile.png"

    def availableMove(self):
        return True

    def afterMove(self):
        return True
