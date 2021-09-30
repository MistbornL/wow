heroes = {
    "Dranei":
        [
            {
                "Paladin":
                    {
                        "Hp": 580,
                        "Mana": 100,
                        "level": 1
                    }
            },

            {
                "Shaman":
                    {
                        "Hp": 500,
                        "mana": 200,
                        "level": 1
                    }
            },

            {
                "Priest":
                    {
                        "Hp": 400,
                        "mana": 300,
                        "level": 1
                    }
            },

            {
                "Warrior":
                    {
                        "Hp": 500,
                        "rage": 0,
                        "level": 1
                    }
            },
        ],

    "Night Elf":
            [
                {
                    "Rogue":
                        {
                            "Hp": 480,
                            "Energy": 100,
                            "level": 1
                        }
                },

                {
                    "Hunter":
                        {
                            "Hp": 4800,
                            "concentration": 100,
                            "level": 1
                        }
                },

                {
                    "Priest":
                        {
                            "Hp": 400,
                            "mana": 300,
                            "level": 1
                        }
                },

                {
                    "Warrior":
                        {
                            "Hp": 500,
                            "rage": 0,
                            "level": 1
                        }
                },
            ],

    "Gnome":
        [
            {
                "Paladin":
                    {
                        "Hp": 580,
                        "Mana": 100,
                        "level": 1
                    }
            },

            {
                "Shaman":
                    {
                        "Hp": 500,
                        "mana": 200,
                        "level": 1
                    }
            },

            {
                "Rogue":
                    {
                        "Hp": 400,
                        "Energy": 100,
                        "level": 1
                    }
            },

            {
                "Warrior":
                    {
                        "Hp": 500,
                        "rage": 0,
                        "level": 1
                    }
            },
        ],

    "Human":
        [
            {
                "Paladin":
                    {
                        "Hp": 580,
                        "Mana": 100,
                        "level": 1
                    }
            },

            {
                "Hunter":
                    {
                        "Hp": 480,
                        "Concentration": 100,
                        "level": 1
                    }
            },

            {
                "Priest":
                    {
                        "Hp": 400,
                        "mana": 300,
                        "level": 1
                    }
            },

            {
                "Warrior":
                    {
                        "Hp": 500,
                        "rage": 0,
                        "level": 1
                    }
            },
        ]
}


class Player:
    def __init__(self):
        self.race = input("Choose Race: Night Elf, Gnome, Human, Dranei >> ")
        self.klas = None
        self.hp = None
        self.name = input("Enter YOur Character Name >> ")
        self.options = []

        for item in heroes[self.race]:
            for klasebi in item.keys():
                self.options.append(klasebi)

        def choose_class(self):
            if self.race in heroes:
                self.klas = input(f"Classes to choose: {self.options} >> ")
                for hero in heroes[self.race]:
                    self.hp = hero[self.klas]["Hp"]

        try:
            if self.race == "Night Elf":
                choose_class(self)

            elif self.race == "Gnome":
                choose_class(self)

            elif self.race == "Human":
                choose_class(self)

            elif self.race == "Dranei":
                choose_class(self)
        except KeyError:
            pass

    def info(self):
        print(f"Race: {self.race}, HP: {self.hp}, Class: {self.klas}, Name: {self.name}")


p1 = Player()


p1.info()