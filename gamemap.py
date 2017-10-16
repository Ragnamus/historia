import random
from e_tile import TileType

class Gamemap():
    def __init__(self):
        self.grid = []
        self.width = 0
        self.height = 0
        self.actorgrid = []
        self.woodgrid = []

    def add_small_random_forest(self):
        if not woodgrid:
            return
        for c in woodgrid:
            for


    def random_grass_sq(self, size, p_len):
        self.grid = []
        # generate a map of grass, square of dimensions size
        for c in range(size):
            # fill grass for now
            row = []
            a_row = []
            w_row = []
            for r in range(size):
                a_row.append([])
                w_row.append(0)
                r_no = random.random()
                if r_no < p_len:
                    row.append(TileType.LGRASS)
                else:
                    row.append(TileType.GRASS)
            self.grid.append(row)
            self.actorgrid.append(a_row)
            self.woodgrid.append(w_row)
        self.width = size
        self.height = size
