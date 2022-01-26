from Service.choose_class import choose_class

from Service.heroes import heroes, spellBook


class Player:
    def __init__(self):
        self.race = input("Choose Race: Night Elf, Gnome, Human, Dranei >> ")
        self.klas = "Rogue"
        self.name = input("Enter YOur Character Name >> ")
        self.options = []
        self.stats = []

        for hero in heroes[self.race]:
            for klasebi in hero.keys():
                self.options.append(klasebi)

        for hero in heroes[self.race]:
            try:
                self.stats.append(hero[self.klas])
            except KeyError:
                pass

    def choose_class_for_race(self, ):
        if self.race in heroes:
            self.klas = input(f"Classes to choose: {self.options} >> ")

    def info(self):
        print(f"Race: {self.race}, stats: {self.stats}, Class: {self.klas}, Name: {self.name}")

    def spell_book(self):
        if self.klas in spellBook:
            print(f"Spells: {spellBook[self.klas]}")


p1 = Player()

p1.info()
p1.spell_book()
