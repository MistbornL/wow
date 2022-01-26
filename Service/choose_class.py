from typing import List


def choose_class(self, heroes: List):
    if self.race in heroes:
        self.klas = input(f"Classes to choose: {self.options} >> ")
        for hero in heroes[self.race]:
            self.hp = hero[self.klas]["Hp"]
        print(self.klas)