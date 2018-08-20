import actor
from e_tile import TileType
import calendar
from e_culture import Culture


class Settlement(actor.Actor):
    def __init__(self, x, y, culture, sid, date):
        self.id = TileType.HAMLET
        self.posx = x
        self.posy = y
        self.type = 'Hamlet'
        self.soc_id = sid
        self.building_list = []
        self.villager_list = []
        self.resource_dict = {}
        self.army_list = []
        self.founding = date
        self.population = 0
        self.capacity = 0
        self.culture = culture
        self.movable = False
        self.name = self.__generate_random_name()
        self.max_size = 12

        self.housing_score = 0


        if self.culture == Culture.GREEK:
            pass

    def __generate_random_name(self):
        if self.culture == Culture.GREEK:
            return 'Olympus'

    def setstats(self, time):
        pass

    def add_housing(self, size, quality=1):
        self.housing_score += size
        self.capacity = self.housing_score * 10

    def add_citizen(self, villager):
        self.villager_list.append(villager)
        self.population += len(villager.poplist)

    def populate_new_random(self):
        pass
