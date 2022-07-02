import json

def open_json(filename):
	print(filename)
	with open(filename) as json_file:
		return json.load(json_file)

def save_json(filename="", json_data={}):
	with open(filename, "w") as json_file:
		json.dump(json_data, json_file, indent=4)
