import os, json

def main():
	id = input("id: ")
	people = os.listdir("./people/")
	fleNum = 0
	for fle in people:
		print(fleNum, "-", fle)
		fleNum += 1
	file = people[int(input("\nfile number: "))]
	output = checkIfThere(id, file)
	print(output)

def checkIfThere(idToSearch,fileName):
	with open("./people/"+fileName) as f:
		file = json.load(f)
		mainName = fileName.strip(".json")
		if idToSearch in file:
			return mainName + " -> " + idToSearch
		for id in file:
			if idToSearch in file[id]:
				return mainName + " -> " + id + " -> " + idToSearch
		for id in file:
			for idd in file[id]:
				if idToSearch in file[id][idd]:
					return mainName + " -> " + id + " -> " + idd + " -> " + idToSearch
	return "nothing found?"
				
# print(checkIfThere("76561198199384013", "76561198967207139-300k.json"))