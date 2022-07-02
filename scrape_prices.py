
from os import listdir
from random import randint
from time import sleep

from figure import Figure
from solaris_japan import Solaris_Japan
import data_functions as data_func

def scraper(file_id):
	FIG_FOLDER = "./Figures/"
	filename = file_id if ".json" in file_id else file_id + ".json"
	if filename in listdir(FIG_FOLDER):
		fig = Figure(file_id.replace(".json", ""))
		fig_url = fig.data["Websites"]["Solaris Japan"]["URL"]
		solaris = Solaris_Japan(fig_url)

		fig.data["Websites"]["Solaris Japan"] = {
			"URL": fig.data["Websites"]["Solaris Japan"]["URL"]
		}
		for price in solaris.prices:
			fig.data["Websites"]["Solaris Japan"][price] = solaris.prices[price]
		
		data_func.save_json(FIG_FOLDER + filename, fig.data)
		
		random_time = randint(10, 30)

		print(solaris.prices)
		print(random_time, "seconds until next figure.", "\n")
		sleep(random_time)