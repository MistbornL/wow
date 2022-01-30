def choose_class_for_race(race, heroes, klas, options, stats):
    if race in heroes:
        klas = input(f"Classes to choose: {options} >> ")
        for classes in heroes[race]:
            for item in classes:
                if item == klas:
                    stats = classes[klas]
                    return stats
