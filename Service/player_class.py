from Service.heroes import heroes, spellBook


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

    def choose_class_for_race(self):
        if self.race in heroes:
            self.klas = input(f"Classes to choose: {self.options} >> ")
            for classes in heroes[self.race]:
                for item in classes:
                    if item == self.klas:
                        self.stats = classes[self.klas]

    def info(self):
        print(f"Race: {self.race}, stats: {self.stats}, Class: {self.klas}, Name: {self.name}")

    def spell_book(self):
        if self.klas in spellBook:
            print(f"Spells: {spellBook[self.klas]}")
