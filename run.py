from os import listdir

from scrape_prices import scraper
import data_functions as data_func

FIG_FOLDER = "./Figures/"

# def scrape_by_
figure_collection = data_func.open_json("./my_figures.json")

for category in figure_collection:
	for fig_no in figure_collection[category]:
		scraper(fig_no)
		

# for fig_no in listdir(FIG_FOLDER):
# 	scraper(fig_no)


