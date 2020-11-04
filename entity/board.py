from entity.cell import Cell

class Board:
    ''' représentation of the board '''
    def __init__(self, cells:[Cell]):
        self.cells = cells

    def move(self):
        return True

    def initPlace(self):
        self.initYellowTeam()
        self.initRedTeam()
        self.initBlueTeam()
        self.initGreenTeam()

    def initRedTeam(self):
        return True

    def initYellowTeam(self):
        return True

    def initBlueTeam(self):
        return True

    def initGreenTeam(self):
        return True
