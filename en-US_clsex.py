class Personnel():
	personnel_list=[]

	def __init__(self,name):
		self.name=name
		self.abilities=[]
		self.add_personnel()
	@classmethod
	def view_personnel_number(cls):
		print(len(cls.personnel_list))

	def add_personnel(self):
		self.personnel_list.append(self.name)
		print("{} is added to personnel list!".format(self.name))

	@classmethod
	def view_personnels(cls):
		print("Personnel list: ")
		for person in cls.personnel_list:
			print(person)

	def add_ability(self,ability):
		self.abilities.append(ability)

	def kabiliyetleri_görüntüle(self):
		print("{}'s abilities: ".format(self.name))
		for ability in self.abilities:
			print(ability)