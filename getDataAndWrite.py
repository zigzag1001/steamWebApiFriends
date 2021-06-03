import requests
import json
import os
import time

# file path for steam id jsons
filePath = "./people/"
key = input("paste in key:\n")

startTime = time.time()
seenUsers = []
usersSeenTwice = 0
uniqueUsers = 0

# gets friends of input steam id, returns dict
def getFriendList(steamid):
	global seenUsers
	global usersSeenTwice
	global uniqueUsers

	numOfFriends = 0
	
	new = {}
	
	# data required for request
	data = {'key': str(key),
	'steamid': str(steamid),
	'relationship': 'friend'}

	# url which request is sent to
	url = "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key="+data['key']+"&steamid="+data['steamid']+"&relationship=friend"
	
	# send request and save the data to req
	req = requests.get(url, data = data).text

	# if profile is private return empty dict
	if req == '{}':
		return {}

	# loading requested info as json
	another = json.loads(req)
	
	# filtering out everything else except steam id
	for friend in another['friendslist']['friends']:
		if not friend['steamid'] in seenUsers:
			new[friend['steamid']] = ''
			seenUsers.append(friend['steamid'])
			uniqueUsers += 1
		else:
			usersSeenTwice += 1

	# returns filtered dict
	return new

# writes friends to new file
def writeToFile(full, steamid):
	
	new = {}
	
	steamidFileName = filePath + steamid + ".json"
	if os.path.isfile(steamidFileName):
		os.remove(steamidFileName)

	with open(steamidFileName, "w") as file:
		json.dump(full, file, indent = 2)

# loads friends list and gets friends of every friend of initial user
def getFoF(fileName):

	# adds .json to end of steamid
	if not ".json" in fileName:
		fileName += ".json"

	# opends file and gets friends of every friend of initial user
	with open(filePath + fileName) as f:
		ids = json.load(f)
		for id in ids:
			ids[id] = getFriendList(id)
		# print("===")
		return ids

# loads friends list and gets friends of friends of every friend of initial user
def getFoFoF(fileName):

	# adds .json to end of steamid
	if not ".json" in fileName:
		fileName += ".json"

	# opends file and gets friends of friends of every friend of initial user
	with open(filePath + fileName) as f:
		ids = json.load(f)
		copy = ids
		for id in ids:
			for idd in ids[id]:
				ids[id][idd] = getFriendList(idd)
			with open(filePath + fileName, "w") as n:
				json.dump(ids, n, indent = 2)
				if os.path.getsize(filePath+fileName) > 10000000:
					return ids
		# print("===")
		return ids

# steamid
id = "76561198967207139"

print("started")

# generates initial json file with friends of input id
writeToFile(getFriendList(id), id)

# gets friends of friends and dumps into the same json file
toDump = getFoF(id)
with open(filePath + id + ".json", "w") as file:
	json.dump(toDump, file, indent = 2)

input("press enter to continue to big boi")
print("started big boi")

toDump = getFoFoF(id)
with open(filePath + id + ".json", "w") as file:
	json.dump(toDump, file, indent = 2)

print("last task done in", time.time()-startTime)
print("unique users:",uniqueUsers)
print("skipped users:",usersSeenTwice)