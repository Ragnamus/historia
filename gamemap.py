import random
from e_tile import TileType
import numpy as np

class Gamemap():
    def __init__(self, size, p_len):
        self.grid = []
        self.actorgrid = []
        self.width = 0
        self.height = 0
        self.random_grass_sq(size, p_len)
        self.woodgrid = np.zeros((self.height, self.width,))
        self.watergrid = np.zeros((self.height+1, self.width+1,))

    def add_random_forest(self, clusters, size):

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

        path = []

        rx = random.randint(0, self.width-1)
        ry = random.randint(0, self.height-1)
        #rx = ry = 20
        fx = float(rx)
        fy = float(ry)
        path.append((rx, ry))
        #print(rx, ry)
        dir = random.random()
        dir *= 2 * np.pi
        sindir = np.sin(dir)
        cosdir = np.cos(dir)
        for e in np.arange(length):
            fx += sindir
            fy += cosdir
            newx = int(fx)
            newy = int(fy)
            if newx < 0 or newx > self.width-1 or newy < 0 or newy > self.height-1:
                break
            if newx == rx and newy == ry:
                continue
            else:
                rx = newx
                ry = newy
                path.append((rx, ry))
        #print(path)

        """assign numbers to grid
        0 - no water
        1 - top left - 91
        2 - left to right - 92
        3 - top right - 93
        4 - up to down - 98
        5 - cross - 99
        6 - not used
        7 - bottom left - 105
        8 - not used
        9 - bottom right - 107
        10 - t top - 94
        11 - t left - 102
        12 - t right - 101
        13 - t bottom - 95
        """
        #self.watergrid[30, 30] = 92

        def r_step(c):
            if self.watergrid[c[0]-1, c[1]] > 0:
                self.watergrid[c[0], c[1]] = 92
            elif self.watergrid[c[0], c[1]-1] > 0:
                self.watergrid[c[0], c[1]] = 105
            elif self.watergrid[c[0], c[1]+1] > 0:
                self.watergrid[c[0], c[1]] = 91
            else:
                self.watergrid[c[0], c[1]] = 92

        def ul_step(c):
            if random.random() > 0.5:
                self.watergrid[c[0]-1, c[1]] = 105
                if self.watergrid[c[0], c[1]+1] > 0:
                    self.watergrid[c[0], c[1]] = 93
                elif self.watergrid[c[0]+1, c[1]] > 0:
                    self.watergrid[c[0], c[1]] = 92
            else:
                self.watergrid[c[0], c[1]-1] = 93
                if self.watergrid[c[0], c[1]+1] > 0:
                    self.watergrid[c[0], c[1]] = 98
                elif self.watergrid[c[0]+1, c[1]] > 0:
                    self.watergrid[c[0], c[1]] = 105

        def u_step(c):
            if self.watergrid[c[0]-1, c[1]] > 0:
                self.watergrid[c[0], c[1]] = 107
            elif self.watergrid[c[0]+1, c[1]] > 0:
                self.watergrid[c[0], c[1]] = 105
            elif self.watergrid[c[0], c[1]+1] > 0:
                self.watergrid[c[0], c[1]] = 98
            else:
                self.watergrid[c[0], c[1]] = 98

        def ur_step(c):
            if random.random() > 0.5:
                self.watergrid[c[0]+1, c[1]] = 107
                if self.watergrid[c[0], c[1]+1] > 0:
                    self.watergrid[c[0], c[1]] = 91
                elif self.watergrid[c[0]-1, c[1]] > 0:
                    self.watergrid[c[0], c[1]] = 92
            else:
                self.watergrid[c[0], c[1]-1] = 91
                if self.watergrid[c[0], c[1]+1] > 0:
                    self.watergrid[c[0], c[1]] = 98
                elif self.watergrid[c[0]-1, c[1]] > 0:
                    self.watergrid[c[0], c[1]] = 107

        def l_step(c):
            if self.watergrid[c[0]+1, c[1]] > 0:
                self.watergrid[c[0], c[1]] = 92
            elif self.watergrid[c[0], c[1]-1] > 0:
                self.watergrid[c[0], c[1]] = 107
            elif self.watergrid[c[0], c[1]+1] > 0:
                self.watergrid[c[0], c[1]] = 93
            else:
                self.watergrid[c[0], c[1]] = 92

        def dr_step(c):
            if random.random() > 0.5:
                self.watergrid[c[0]+1, c[1]] = 93
                if self.watergrid[c[0], c[1]-1] > 0:
                    self.watergrid[c[0], c[1]] = 105
                elif self.watergrid[c[0]-1, c[1]] > 0:
                    self.watergrid[c[0], c[1]] = 92
            else:
                self.watergrid[c[0], c[1]+1] = 105
                if self.watergrid[c[0], c[1]-1] > 0:
                    self.watergrid[c[0], c[1]] = 98
                elif self.watergrid[c[0]-1, c[1]] > 0:
                    self.watergrid[c[0], c[1]] = 93

        def d_step(c):
            if self.watergrid[c[0]+1, c[1]] > 0:
                self.watergrid[c[0], c[1]] = 91
            elif self.watergrid[c[0], c[1]-1] > 0:
                self.watergrid[c[0], c[1]] = 98
            elif self.watergrid[c[0]-1, c[1]] > 0:
                self.watergrid[c[0], c[1]] = 93
            else:
                self.watergrid[c[0], c[1]] = 98

        def dl_step(c):
            if random.random() > 0.5:
                self.watergrid[c[0]-1, c[1]] = 91
                if self.watergrid[c[0], c[1]-1] > 0:
                    self.watergrid[c[0], c[1]] = 107
                elif self.watergrid[c[0]+1, c[1]] > 0:
                    self.watergrid[c[0], c[1]] = 92
            else:
                self.watergrid[c[0], c[1]+1] = 107
                if self.watergrid[c[0], c[1]-1] > 0:
                    self.watergrid[c[0], c[1]] = 98
                elif self.watergrid[c[0]+1, c[1]] > 0:
                    self.watergrid[c[0], c[1]] = 91



        for i, c in enumerate(path[:-1]):
            # look forwards and backwards
            f = path[i+1]
            d = ((f[1] - c[1]) * 3) + (f[0] - c[0])
            #print(d)

            p_switch = {
                1: r_step,
                2: dl_step,
                3: d_step,
                4: dr_step,
                -1: l_step,
                -2: ur_step,
                -3: u_step,
                -4: ul_step
            }

            f = p_switch.get(d, lambda: "nothing")
            f(c)

        #print final one without looking forwards
        (lx, ly) = path[-1]
        if self.watergrid[lx-1, ly] > 0:
            if ly == 0:
                self.watergrid[lx, ly] = 107
            elif ly == self.height - 1:
                self.watergrid[lx, ly] = 93
            else:
                self.watergrid[lx, ly] = 92
        elif self.watergrid[lx+1, ly] > 0:
            if ly == 0:
                self.watergrid[lx, ly] = 105
            elif ly == self.height - 1:
                self.watergrid[lx, ly] = 91
            else:
                self.watergrid[lx, ly] = 92
        elif self.watergrid[lx, ly-1] > 0:
            if lx == 0:
                self.watergrid[lx, ly] = 107
            elif lx == self.width - 1:
                self.watergrid[lx, ly] = 105
            else:
                self.watergrid[lx, ly] = 98
        elif self.watergrid[lx, ly+1] > 0:
            if lx == 0:
                self.watergrid[lx, ly] = 93
            elif lx == self.width - 1:
                self.watergrid[lx, ly] = 91
            else:
                self.watergrid[lx, ly] = 98



    def print_water(self):
        print(self.watergrid)

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
    testmap.random_grass_sq(20, 0.1)
    testmap.add_random_river(20)
    testmap.print_water()
