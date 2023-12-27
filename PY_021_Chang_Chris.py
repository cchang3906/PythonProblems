class album:
	def __init__(self, name, title, songs=None):
		self.name = name.title()
		self.title = title.title()
		self.songs =  songs

	def describe(self):
		if self.songs:
			print(f"{self.name}, {self.title}, {self.songs} songs")
		else:
			print(f"{self.name}, {self.title}")

viv_album = album('vivaldi', 'winter')
trav_album = album('astroworld', 'travis scott', 17)
curr_album = album('currents', 'the way it ends', 11)
viv_album.describe()
trav_album.describe()
curr_album.describe()