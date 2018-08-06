import sys

from room import Room
from item import Item
from character import Enemy
from character import Friend
from item import Item

backpack = []

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

dan = Friend("Dan the Mushroom Man", "A friendly purveyor of mushrooms.")
dan.set_conversation("Hello, please buy my freshly grown mushrooms. They are grown from my own body!")
kitchen.set_character(dan)

frostmourne = Item("Frostmourne", "Whomsoever takes up this blade shall wield power eternal. Just as the blade rends flesh, so must power scar the spirit.")
ballroom.set_item(frostmourne)

current_room = kitchen

def talk_to_inhabitant(inhabitant):
	if inhabitant is not None:
		inhabitant.talk()
	else:
		print("You whisper to yourself quietly, since there is no-one else to talk to. Would you like to do something else?")

def fight_dat_bad_boi(inhabitant):
	if inhabitant is not None and isinstance(inhabitant,Enemy):
		print("What will you fight with?")
		fight_with = input("> ")
		if inhabitant.fight(fight_with):
			current_room.set_character(None)
			inhabitant.is_defeated()
			inhabitant.get_status()
		else:
			print("You're dead. Bye.")
			sys.exit(0)
	elif inhabitant is None:
		print("You punch the air around you, since there is no-one to fight. Would you like to do something else?")
	elif isinstance(inhabitant, Friend):
		print(inhabitant.name + " doesn't want to fight with you. They're friendly.")
		return True

def sleep_enemy(inhabitant):
	if inhabitant is not None and isinstance(inhabitant,Enemy):
			inhabitant.sleep()
			if inhabitant.get_sleep() == True:
				print(inhabitant.name + " is dribbling in their sleep.")
			else:
				print(inhabitant.name + " looks angry. There was no honour in that. They raise their weapon!")
				fight_dat_bad_boi(inhabitant)
	else:
		print("Please don't put " + inhabitant.name + " to sleep. They're a friend :(")

def hug_inhabitant(inhabitant):
	if inhabitant is not None and isinstance(inhabitant,Friend):
		inhabitant.hug()
	else:
		print(inhabitant.name + " looks offended. They don't want to hug you. Sorry.")

def take_item(item):
	if item is not None and item.in_room == True:
		backpack.append(item)
		item.in_room = False
	else:
		print("There is nothing to pick up.")

def inventory():
	if len(backpack) == 0:
		print("Your bag is empty.")
	else:
		for item in backpack:
			print("[Inventory]: " + item.name)


#print a new line, gets details, makes whatever the player types a variable and moves in that direction
while True:
	print("\n")
	current_room.get_details()
	inhabitant = current_room.get_character()
	item = current_room.get_item()
	if inhabitant is not None:
		inhabitant.describe()
	if item is not None and item.in_room == True:
		item.describe_item()
	command = input("> ")
	if command in ["north", "south", "east", "west"]:
		current_room = current_room.move(command)
	elif command == "talk":
		talk_to_inhabitant(inhabitant)
	elif command == "fight":
		fight_dat_bad_boi(inhabitant)
	elif command == "sleep":
		sleep_enemy(inhabitant)
	elif command == "hug":
		hug_inhabitant(inhabitant)
	elif command == "take":
		take_item(item)
	elif command == "inventory":
		inventory()
