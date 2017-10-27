import random
from e_tile import TileType
import numpy as np

class Gamemap():
    def __init__(self):
        self.grid = []
        self.width = 0
        self.height = 0
        self.actorgrid = []
        self.woodgrid = None
        self.rivergrid = None

    def add_random_forest(self, clusters, size):
        self.woodgrid = np.zeros((self.height, self.width,))

        for c in np.arange(clusters):
            rx = random.randint(0, self.width-1)
            ry = random.randint(0, self.height-1)
            #print(rx, ry)
            self.woodgrid[ry][rx] = 1

        for i in np.arange(size):
            wg_tempw = np.roll(self.woodgrid, -1, axis=0)
            wg_tempw[-1,:] = 0
            #print(wg_tempw)
            wg_tempa = np.roll(self.woodgrid, -1, axis=1)
            wg_tempa[:,-1] = 0
            #print(wg_tempa)
            wg_temps = np.roll(self.woodgrid, 1, axis=0)
            wg_temps[0,:] = 0
            #print(wg_temps)
            wg_tempd = np.roll(self.woodgrid, 1, axis=1)
            wg_tempd[:,0] = 0
            #print(wg_tempd)

            rand_matw = np.random.random((self.width, self.height,))
            rand_mata = np.random.random((self.width, self.height,))
            rand_mats = np.random.random((self.width, self.height,))
            rand_matd = np.random.random((self.width, self.height,))

            wg_tempw = np.rint(np.divide(np.multiply(rand_matw, wg_tempw),
                               self.woodgrid ** 2 + 1))
            wg_tempa = np.rint(np.divide(np.multiply(rand_matw, wg_tempa),
                               self.woodgrid ** 2 + 1))
            wg_temps = np.rint(np.divide(np.multiply(rand_matw, wg_temps),
                               self.woodgrid ** 2 + 1))
            wg_tempd = np.rint(np.divide(np.multiply(rand_matw, wg_tempd),
                               self.woodgrid ** 2 + 1))

            self.woodgrid = np.add(np.add(np.add(np.add(self.woodgrid,
                                   wg_tempw), wg_tempa), wg_temps), wg_tempd)


    def print_forests(self):
        print(self.woodgrid)

    def add_random_river(self, length):
        self.rivergrid = np.zeros((self.height, self.width,))

        rx = random.randint(0, self.width-1)
        ry = random.randint(0, self.height-1)
        #print(rx, ry)
        if random.random() < 0.5:
            self.rivergrid[ry][rx] = 92
        else:
            self.rivergrid[ry][rx] = 98

        

        for l in np.arange(length):




    def random_grass_sq(self, size, p_len):
        self.grid = []
        # generate a map of grass, square of dimensions size
        for c in range(size):
            # fill grass for now
            row = []
            a_row = []
            for r in range(size):
                a_row.append([])
                r_no = random.random()
                if r_no < p_len:
                    row.append(TileType.LGRASS)
                else:
                    row.append(TileType.GRASS)
            self.grid.append(row)
            self.actorgrid.append(a_row)
        self.width = size
        self.height = size

if __name__ == '__main__':
    testmap = Gamemap()
    testmap.random_grass_sq(15, 0.1)
    testmap.add_random_forest(8, 4)
    testmap.print_forests()
