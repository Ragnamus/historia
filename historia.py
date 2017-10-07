from bearlibterminal import terminal as blt
from e_tile import TileType
import random
import camera
import gamemap
import cursor
import console


class historia():
    """
    CLASS: main historia class
    """
    def __init__(self):
        self.gmap = gamemap.Gamemap()
        self.camera = camera.Camera(40, 40)
        self.cursor = cursor.Cursor()
        self.console = console.Console()

        self.mouse_x = 0
        self.mouse_y = 0

    def setup(self):
        print("setup...")
        blt.open()

        # set title
        blt.set("""
                window: size=160x40,
                cellsize=auto,
                font:default""")

        blt.set("window.title='historia'")
        blt.set("input.filter={keyboard, mouse+}")
        blt.clear()
        blt.color("white")

        # load tilesets
        blt.set("U+E000: toen.png, size=16x16, align=top-left")

        # set up map
        self.gmap.random_grass_sq(60, 0.1)

    def hello(self):
        blt.printf(1, 1, 'Hello World')
        blt.refresh()

    def tile_test(self):
        blt.put(1, 3, 0xE000+0)
        blt.put(3, 3, 0xE000+2)
        blt.refresh()

    def print_grid(self):
        blt.layer(1)
        blt.clear()
        for r, row in enumerate(range(self.camera.height)):
            for c, element in enumerate(range(self.camera.width)):
                gridx = c + self.camera.posx
                gridy = r + self.camera.posy
                # print(type(hex(self.gmap.grid[gridx][gridy].value)))
                # print(type(0xE000))
                hexcode = 0xE000 + self.gmap.grid[gridx][gridy].value
                blt.put(c * 2, r, hexcode)

    def print_overlay(self):
        blt.layer(4)
        blt.clear_area(0, 0, self.camera.width, self.camera.height)
        selectcode = 0xE000 + TileType.SELECTY.value
        # selection
        blt.put(self.cursor.x * 2, self.cursor.y, selectcode)

        # info part
        x = self.cursor.x + self.camera.posx
        y = self.cursor.y + self.camera.posy
        blt.puts(82, 1, "(%d, %d)" % (x, y))
        blt.puts(82, 3, self.console.get_info(self.gmap, x, y))

    def mainloop(self):
        # print map
        self.print_grid()
        # print overlay
        self.print_overlay()

        # after printing, refresh
        blt.refresh()

        key = blt.read()
        if key in (blt.TK_CLOSE, blt.TK_ESCAPE):
            game_loop = 0
        else:
            if (key == blt.TK_RIGHT and
                    self.camera.posx <
                    self.gmap.width - self.camera.width):

                self.camera.posx += 1
                # print(self.camera.posx, self.camera.posy)

            elif (key == blt.TK_LEFT and
                  self.camera.posx > 0):

                self.camera.posx -= 1
                # print(self.camera.posx, self.camera.posy)

            elif (key == blt.TK_DOWN and
                  self.camera.posy <
                  self.gmap.height - self.camera.height):

                self.camera.posy += 1
                # print(self.camera.posx, self.camera.posy)

            elif (key == blt.TK_UP and
                  self.camera.posy > 0):

                self.camera.posy -= 1
                # print(self.camera.posx, self.camera.posy)

            elif key == blt.TK_A:
                if self.cursor.x > 0:
                    self.cursor.x -= 1
                elif self.camera.posx > 0:
                    self.camera.posx -= 1
                    # print(self.camera.posx, self.camera.posy)

            elif key == blt.TK_D:
                if self.cursor.x < self.camera.width - 1:
                    self.cursor.x += 1
                elif self.camera.posx < self.gmap.width - self.camera.width:
                    self.camera.posx += 1
                    # print(self.camera.posx, self.camera.posy)

            elif key == blt.TK_W:
                if self.cursor.y > 0:
                    self.cursor.y -= 1
                elif self.camera.posy > 0:
                    self.camera.posy -= 1
                    # print(self.camera.posx, self.camera.posy)

            elif key == blt.TK_S:
                if self.cursor.y < self.camera.height - 1:
                    self.cursor.y += 1
                elif self.camera.posy < self.gmap.height - self.camera.height:
                    self.camera.posy += 1
                    # print(self.camera.posx, self.camera.posy)

            elif key == blt.TK_MOUSE_LEFT:
                self.mouse_x = blt.state(blt.TK_MOUSE_X)
                self.mouse_y = blt.state(blt.TK_MOUSE_Y)
                print(self.mouse_x, self.mouse_y)

            game_loop = 1
        return game_loop


if __name__ == '__main__':
    game = historia()
    # setup game
    game.setup()
    # test
    # game.hello()
    # game.tile_test()
    # main loop
    game_loop = 1
    while game_loop == 1:
        game_loop = game.mainloop()
