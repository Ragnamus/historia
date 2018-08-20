import actor
from e_tile import TileType
from e_person import Gender
import random
import person
import calendar
from e_culture import Culture


class Villager(actor.Actor):
    def __init__(self, x, y, culture, vid, date):
        if random.random() < 0.5:
            self.id = TileType.FVILLAGER
        else:
            self.id = TileType.MVILLAGER
        self.posx = x
        self.posy = y
        self.type = 'Villager'
        self.vil_id = vid
        self.poplist = []
        self.lastdate = date
        self.culture = culture
        self.parent = None
        self.movable = True
        self.mv_max = 4.0
        self.mv_points = self.mv_max

        self.productivity = 0.0

        if self.culture == Culture.GREEK:
            from greek_names_male import GreekNamesMale
            from greek_names_female import GreekNamesFemale
            self.malelist = list(GreekNamesMale)
            self.femalelist = list(GreekNamesFemale)

    def __generate_random_name(self, gender):
        if self.culture == Culture.GREEK:
            if gender == Gender.MALE:
                return random.choice(self.malelist).name
            else:
                return random.choice(self.femalelist).name

    def __generate_random_surname(self):
        return ''

    def setparent(self, settlement):
        # set settlement where the villager lives
        self.parent = settlement
        self.parent.add_citizen(self)

    def setstats(self, time):
        # productivity
        infant = 0
        child = 0
        young_adult = 0
        adult = 0
        elder = 0
        infirm = 0
        for person in self.poplist:
            age = person.birth.getAge(time)
            if age < 8:
                infant += 1
            elif age < 14:
                child += 1
            elif age < 20:
                young_adult += 1
            elif age < 36:
                adult += 1
            elif age < 52:
                elder += 1
            else:
                infirm += 1
        self.productivity = ((infant * (-0.3)) + (young_adult * 1.2) +
                             (adult * 1.0) + (elder * 0.8) + (infirm * (-0.2)))


    def populate_new_random(self, N, mu, sigma, mu_eld=0, mu_chd=3.0):
        nm = 0
        nf = 0
        for p in range(N):
            if random.random() < 0.5:
                gender = Gender.MALE
                nm += 1
            else:
                gender = Gender.FEMALE
                nf += 1
            name = self.__generate_random_name(gender)
            family_name = self.__generate_random_surname()
            birth = calendar.Calendar(floatval=self.lastdate.toFloat() -
                                      random.gauss(mu, sigma))
            ch = person.Person(birth, gender, name, family_name)
            self.poplist.append(ch)

        # add children
        nchd = int(nf * mu_chd)
        for c in range(nchd):
            age = random.gauss(mu-18, sigma)
            if age < 0.0:
                continue
            birth = calendar.Calendar(floatval=self.lastdate.toFloat() - age)

            if random.random() < 0.5:
                gender = Gender.MALE
            else:
                gender = Gender.FEMALE
            name = self.__generate_random_name(gender)
            family_name = self.__generate_random_surname()
            ch = person.Person(birth, gender, name, family_name)
            self.poplist.append(ch)
