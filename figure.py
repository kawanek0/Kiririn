import os
from pprint import pprint

import data_functions as data_func
from solaris_japan import Solaris_Japan

class Figure:
	def __init__(self, fig_id):
		self.fig_id = fig_id
		self.file_format = str(fig_id) + ".json"
		self.get_data_from_json()
		self.prices = {}

	# Getting figure data
	def check_character(self):
		file = "./Figures/" + self.file_format
		no_char = "No figure in index.'"
		return file if os.path.isfile(file) else no_char

	def get_data_from_json(self):
		self.file = self.check_character()
		if self.file != "No figure in index.'":
			self.data = data_func.open_json(self.file)
		else:
			self.data = {}

	# Scraping prices
	def get_solaris(self):
		self.prices["Solaris Japan"] = {
			"URL": self.data["Websites"]["Solaris Japan"]["URL"]
		}
		self.solaris = Solaris_Japan(self.prices["Solaris Japan"]["URL"])
		
		for price in self.solaris.prices:
			self.prices["Solaris Japan"][price] = self.solaris.prices[price]

		self.data["Websites"]["Solaris Japan"] = self.prices["Solaris Japan"]

	def get_nin_nin(self):
		pass

