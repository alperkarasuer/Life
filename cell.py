import random

class Cell(object):
    cellObjs = []  # registrar
    def __init__(self, cellPos, gameInfo):
        '''
        Cell has the ability to be alive or dead, status can be
        checked with functions. Initial status is dead.
        '''
        Cell.cellObjs.append(self)
        self.width = gameInfo[0]
        self.height = gameInfo[1]
        self.margin = gameInfo[2]
        self.rowPos = cellPos[0]
        self.colPos = cellPos[1]
        self._status = 'Dead'
        self.screenPos = [[(self.colPos+1)*self.margin + self.colPos*self.width,
                           (self.colPos+1)*self.margin + (self.colPos+1)*self.width],
                          [(self.rowPos+1)*self.margin + self.rowPos*self.height,
                           (self.rowPos+1)*self.margin + (self.rowPos+1)*self.height]]

    @classmethod
    def randomGenerate(cls):
        for obj in cls.cellObjs:
            if random.uniform(0,1) > 0.5:
                obj.set_alive()

    @classmethod
    def clear_all(cls):
        for obj in cls.cellObjs:
            obj.set_dead()

    def set_dead(self):
        self._status = 'Dead'

    def set_alive(self):
        self._status = 'Alive'

    def is_alive(self):
        return True if self._status == 'Alive' else False