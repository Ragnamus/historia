import gamemap
from e_tile import TileType

class Console():
    def __init__(self):
        self.status = 1

    def get_info(self, gamemap, x, y):
        return gamemap.grid[x][y].name
