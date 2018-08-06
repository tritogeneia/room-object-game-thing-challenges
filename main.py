import sys

from room import Room
from item import Item
from character import Enemy

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("Skeletons sit at their seats, their cracked and yellowing skulls staring at the goblets of wine they never got to finish.")

ballroom = Room("Ballroom")
ballroom.set_description("The glow of the moonlight that shines through the dingy windows catches each speck of dust in the air, making the spiderwebs that cling to the abandoned chairs glisten.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

sylv = Enemy("Sylvanas", "A smelly, dirty, morally grey banshee zombie lady.")
sylv.set_conversation("BURN IT!")
sylv.set_weakness("Frostmourne")

dining_hall.set_character(sylv)

current_room = kitchen

def talk_to_inhabitant(inhabitant):
	if inhabitant is not None:
		inhabitant.talk()
	else:
		print("You whisper to yourself quietly, since there is no-one else to talk to. Would you like to do something else?")

def fight_dat_bad_boi(inhabitant):
	if inhabitant is not None:
		print("What will you fight with?")
		fight_with = input("> ")
		if inhabitant.fight(fight_with):
			current_room.set_character(None)
		else:
			print("You're dead. Bye.")
			sys.exit(0)
	else:
		print("You punch the air around you, since there is no-one to fight. Would you like to do something else?")


#print a new line, gets details, makes whatever the player types a variable and moves in that direction
while True:
	print("\n")
	current_room.get_details()
	inhabitant = current_room.get_character()
	if inhabitant is not None:
		inhabitant.describe()
	command = input("> ")
	if command in ["north", "south", "east", "west"]:
		current_room = current_room.move(command)
	elif command == "talk":
		talk_to_inhabitant(inhabitant)
	elif command == "fight":
		fight_dat_bad_boi(inhabitant)
	elif command == "sleep":
		if inhabitant is not None:
			inhabitant.sleep()
			if inhabitant.get_sleep() == True:
				print(inhabitant.name + " is dribbling in their sleep.")
			else:
				print(inhabitant.name + " looks angry. There was no honour in that. They raise their weapon!")
				fight_dat_bad_boi(inhabitant)

