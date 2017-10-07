import actor
from e_tile import TileType
from e_person import Gender
import random
import person


class Villager(actor.Actor):
    def __init__(self, x, y, vid, date):
        if random.random() < 0.5:
            self.id = TileType.FVILLAGER
        else:
            self.id = TileType.MVILLAGER
        self.posx = x
        self.posy = y
        self.vil_id = vid
        self.poplist = []
        self.lastdate = date

    def __generate_random_name(self, gender):
        if gender == Gender.MALE:
            return 'John'
        else:
            return 'Clare'

    def __generate_random_surname(self):
        return 'Smith'

    def populate_new_random(self, N, mu, sigma, p_marriedu_eld=0, mu_chd=3.0):
        for p in range(N):
            if random.random() < 0.5:
                gender = Gender.MALE
            else:
                gender = Gender.FEMALE
            name = self.__generate_random_name(gender)
            family_name = self.__generate_random_surname()
            birth = self.lastdate - random.gauss(mu, sigma)
            ch = person.Person(birth, gender, name, family_name)
            self.poplist.append(ch)
