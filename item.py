class Item():
	def __init__(self, item_name, item_description):
		self.name = item_name
		self.description = item_description
		self.in_room = True

	def describe_item(self):
		print("You find " + self.name + "!")
		print(self.description)
		print("-------------")
	
		