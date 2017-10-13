from bearlibterminal import terminal as blt
from e_tile import TileType
from e_culture import Culture
from e_person import Gender
import random
import camera
import gamemap
import cursor
import console
import actor
import villager
import calendar


class historia():
    """
    CLASS: main historia class
    """
    def __init__(self):
        self.gmap = gamemap.Gamemap()
        self.camera = camera.Camera(40, 40)
        self.cursor = cursor.Cursor()
        self.console = console.Console()
        self.actor_list = []

        self.mouse_x = 0
        self.mouse_y = 0

        self.time = calendar.Calendar()

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

    def basic_start(self):
        # actor setup

        # create a basic villager token
        vil1 = villager.Villager(10, 10, Culture.GREEK, 1, self.time)
        vil1.populate_new_random(8, 20.0, 3.0)

        self.actor_list.append(vil1)

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

    def print_actors(self):
        blt.layer(2)
        blt.clear_area(0, 0, self.camera.width, self.camera.height)
        for actor in self.actor_list:
            blt.put(actor.posx * 2, actor.posy, 0xE000 + actor.id.value)

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

        for actor in self.actor_list:
            if actor.posx == x and actor.posy == y and actor.type == 'Villager':
                actor.setstats(self.time)
                blt.puts(82, 5, actor.id.name)
                for i, person in enumerate(actor.poplist, 0):
                    blt.puts(82, 6+i, "%s %s" % (person.name, person.surname))
                    if person.gender == Gender.MALE:
                        g = 'M'
                    else:
                        g = 'F'
                    blt.puts(96, 6+i, "%s" % (g))
                    blt.puts(102, 6+i, "Age:%d" % (person.birth.getAge(self.time)))
                blt.puts(82, 26, "Productivity: %g" % (actor.productivity))

    def mouse_interaction(self):
        if self.mouse_x > 0 and self.mouse_x < 200:
            x = self.mouse_x // 2
            y = self.mouse_y
            self.cursor.x = x
            self.cursor.y = y

    def mainloop(self):
        # print map
        self.print_grid()
        # print actors
        self.print_actors()
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
                self.mouse_interaction()

            game_loop = 1
        return game_loop


if __name__ == '__main__':
    game = historia()
    # setup game
    game.setup()
    game.basic_start()
    # test
    # game.hello()
    # game.tile_test()
    # main loop
    game_loop = 1
    while game_loop == 1:
        game_loop = game.mainloop()
