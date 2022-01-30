from Service.choose_race import choose_class_for_race
from classes.player import Player
from Service.heroes import heroes


p1 = Player()

choose_class_for_race(p1.race, heroes, p1.klas, p1.options, p1.stats)
p1.info()
p1.spell_book()
