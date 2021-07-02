import random

class Cell(object):
    cellObjs = []  # registrar
    def __init__(self):
        '''
        Cell has ability to be alive or dead, status can be
        checked with functions. Initial status is dead.
        '''
        Cell.cellObjs.append(self)
        self._status = 'Dead'

    @classmethod
    def randomGenerate(cls):
        for obj in cls.cellObjs:
            if random.uniform(0,1) > 0.5:
                obj.set_alive()

    def set_dead(self):
        self._status = 'Dead'

    def set_alive(self):
        self._status = 'Alive'

    def is_alive(self):
        return True if self._status == 'Alive' else False

    def get_print_character(self):
        return '0' if self.is_alive() else '*'