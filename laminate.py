import numpy as np

class Laminate():
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.move = None

        self.lgrid = np.zeros((width, height,))
        self.lgrid.fill(-1)

    def add_move(self, x, y):
        self.lgrid[x, y] = 0
        self.move = (x, y)

    def reset_move(self):
        self.lgrid = np.zeros((self.width, self.height,))
        self.lgrid.fill(-1)

    def fill_move(self, a):
        def fill(x, y, mp, sp):
            if mp >= sp:
                if self.lgrid[x, y+1] < mp - sp:
                    self.lgrid[x, y+1] = mp - sp
                    fill(x, y+1, mp-sp, sp)
                if self.lgrid[x, y-1] < mp - sp:
                    self.lgrid[x, y-1] = mp - sp
                    fill(x, y-1, mp-sp, sp)
                if self.lgrid[x+1, y] < mp - sp:
                    self.lgrid[x+1, y] = mp - sp
                    fill(x+1, y, mp-sp, sp)
                if self.lgrid[x-1, y] < mp - sp:
                    self.lgrid[x-1, y] = mp - sp
                    fill(x-1, y, mp-sp, sp)

        if self.move:
            x, y = self.move
            mp = a.mv_points
            self.lgrid[x, y] = mp
            fill(x, y, mp, 1.0)
