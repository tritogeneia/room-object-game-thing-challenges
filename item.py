class Item():
	def __init__(self, item_name):
		self.name = item_name
		self.description = None
	def get_item_description(self, item_description):
		self.description = item_description
	def set_item_description(self):
		return self.description
	def describe_item(self):
		print(self.description)