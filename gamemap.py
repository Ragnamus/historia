import random
from e_tile import TileType

class Gamemap():
    def __init__(self):
        self.grid = []
        self.width = 0
        self.height = 0

    def random_grass_sq(self, size, p_len):
        self.grid = []
        # generate a map of grass, square of dimensions size
        for c in range(size):
            # fill grass for now
            row = []
            for r in range(size):
                r_no = random.random()
                if r_no < p_len:
                    row.append(TileType.LGRASS)
                else:
                    row.append(TileType.GRASS)
            self.grid.append(row)
        self.width = size
        self.height = size
