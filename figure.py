
import os
from pprint import pprint

import data_functions as data_func

class Figure:
	def __init__(self, fig_id):
		self.fig_id = fig_id
		self.file_format = str(fig_id) + ".json"
		self.get_data_from_json()

	def get_data_from_json(self):
		self.file = self.check_character()
		if self.file != "No figure in index.'":
			self.data = data_func.open_json(self.file)
		else:
			self.data = {}

	def check_character(self):
		file = "./Figures/" + self.file_format
		no_char = "No figure in index.'"
		return file if os.path.isfile(file) else no_char





# f = Figure(3)

# pprint(f.data)

# data_func.save_json(f.file, f.data)