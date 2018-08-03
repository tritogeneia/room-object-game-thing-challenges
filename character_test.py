from character import Character
from character import Enemy

sylv = Enemy("Sylvanas","A dirty, smelly, morally grey banshee zombie.")
sylv.describe()
sylv.set_conversation("BURN IT!")
sylv.talk()
sylv.set_weakness("Frostmourne")

print("What will you fight with?")
fight_with = input()
sylv.fight(fight_with)