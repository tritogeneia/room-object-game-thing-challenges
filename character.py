import random

class Character():
    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you. They're friendly.")
        return True


class Enemy(Character):
    count = 0
    defeated = 0

    def __init__ (self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.is_sleeping = None
        Enemy.count += 1
    
    def is_defeated(self):
        Enemy.defeated += 1
    
    def get_status(self):
        print(str(Enemy.defeated) + " enemies have been defeated")
    
    def set_weakness(self, weakness):
        self.weakness = weakness
    
    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item.lower() == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item + "!")
            return True
        else:
            print(self.name + " crushes you, puny adventurer.")
            return False
    
    def set_sleep(self, is_sleeping):
        self.is_sleeping = is_sleeping
    
    def get_sleep(self):
        return self.is_sleeping
    
    def sleep(self):
        roll = random.randint(1,100)
        if roll > 50:
            self.set_sleep(True)
            self.description = self.name + " is out cold on the floor."

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
    
    def hug(self):
        print(self.name + " reaches over and gives you a big old hug!")
    