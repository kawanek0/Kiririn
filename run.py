
from os import listdir
from random import randint
from time import sleep

from figure import Figure
from solaris_japan import Solaris_Japan
import data_functions as data_func
from scrape_prices import scraper

FIG_FOLDER = "./Figures/"

for fig_no in listdir(FIG_FOLDER):
	scraper(fig_no)


# for fig_no in listdir(FIG_FOLDER):
# 	if ".json" in fig_no:
# 		fig = Figure(fig_no.replace(".json", ""))
# 		fig_url = fig.data["Websites"]["Solaris Japan"]["URL"]
# 		solaris = Solaris_Japan(fig_url)

# 		fig.data["Websites"]["Solaris Japan"] = {
# 			"URL": fig.data["Websites"]["Solaris Japan"]["URL"]
# 		}
# 		for price in solaris.prices:
# 			fig.data["Websites"]["Solaris Japan"][price] = solaris.prices[price]
		
# 		data_func.save_json(FIG_FOLDER + fig_no, fig.data)
		
# 		random_time = randint(10, 30)

# 		print(solaris.prices)
# 		print(random_time, "seconds until next figure.", "\n")
# 		sleep(random_time)



