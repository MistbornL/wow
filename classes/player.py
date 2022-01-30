from Service.heroes import heroes, spellBook
from Service.choose_race import choose_class_for_race


class Player:
    def __init__(self):
        self.race = input("Choose Race: Night Elf, Gnome, Human, Dranei >> ")
        self.klas = None
        self.name = input("Enter YOur Character Name >> ")
        self.options = []
        self.stats = None

        for hero in heroes[self.race]:
            for klasebi in hero.keys():
                self.options.append(klasebi)

    def info(self):
        print(f"Race: {self.race}, stats: {self.stats}, Class: {self.klas}, Name: {self.name}")

    def spell_book(self):
        if self.klas in spellBook:
            print(f"Spells: {spellBook[self.klas]}")
