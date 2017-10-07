from e_tile import TileType

class Actor:
    def __init__(self, id, x, y):
        self.id = id
        self.posx = x
        self.posy = y
        movable = True
