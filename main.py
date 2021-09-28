heroes = {
    "Dranei":
        ["Paladin", "Shaman", "Priest", "Warrior"],
    "Night Elf":
        ["Hunter", "Druid", "Priest", "Mage", "Rogue"],
    "Gnome":
        ["Mage", "Rogue", "Warlock", "Priest"],
    "Human":
        ["Paladin", "Warrior", "Mage", "Warlock", "Priest", "Rogue"]
}


class Player:
    def __init__(self):
        self.race = input("Choose Race: Night Elf, Gnome, Human, Dranei >> ")
        self.klas = None
        self.hp = None
        self.name = input("Enter YOur Character Name >> ")

        if self.race == "Night Elf":
            self.hp = 400
            if self.race in heroes:
                self.klas = input(f"Classes to choose: {heroes[self.race]} >> ")
        elif self.race == "Gnome":
            self.hp == 380
            if self.race in heroes:
                self.klas = input(f"Classes to choose: {heroes[self.race]} >> ")
        elif self.race == "Human":
            self.hp = 370
            if self.race in heroes:
                self.klas = input(f"Classes to choose: {heroes[self.race]} >> ")
        elif self.race == "Dranei":
            self.hp = 420
            if self.race in heroes:
                self.klas = input(f"Classes to choose: {heroes[self.race]} >> ")

    def info(self):
        print(f"Race: {self.race}, HP: {self.hp}, Class: {self.klas}, Name: {self.name}")


p1 = Player()


p1.info()

