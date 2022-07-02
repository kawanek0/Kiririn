

import requests as req
from time import sleep

from bs4 import BeautifulSoup

class Solaris_Japan:
	def __init__(self, url):
		self.site = "https://solarisjapan.com/products/"
		self.url = url
		self.prices = {}
		self.get_html()
		self.get_avaiablity()

	def get_html(self):
		html = req.get(self.site + self.url)
		self.html = BeautifulSoup(html.content, "html.parser")

	def get_avaiablity(self):
		btn = "button"
		btn_class = {"class": "btn btn__main-content add-js active:!tw-scale-90"}
		self.buttons = self.html.find_all(btn, btn_class)
		for button in self.buttons:
			a = self.parse_availablity(button)
			self.prices[a] = self.get_prices(button)

	def parse_availablity(self, button):
		label = "div"
		btn_label = "product__btn-label"
		label = button.find(label, btn_label)
		labls = ["Pre Order", "Brand New", "Pre Owned"]

		for labl in labls:
			if labl in label.text:
				return labl

	def get_prices(self, button):
		try:
			cost = button.text.strip().split("\n")[-1]
			cost = cost.replace("¥", "")
			cost = cost.replace(",", "")
			cost = cost.replace("$", "")
			cost = int(cost) / 100
		except Exception as e:
			print(e)
			return 0
		return cost

	def get_shipping(self):
		world_shipping = {"class": "worldwide-shipping"}
		a = self.html.find("section", world_shipping)
		print(a.text.replace("\n", " "))


# fig = "kill-la-kill-guts-mankanshoku-mako-nendoroid-408-good-smile-company"
# s = Solaris_Japan(fig)
# s.get_html()
# s.get_avaiablity()
# # print(s.prices)
# s.get_shipping()