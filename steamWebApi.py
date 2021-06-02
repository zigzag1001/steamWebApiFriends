import requests
import json
import os

def getFriendList(steamid):
	if os.path.isfile("TEMPfriends.json"):
		os.remove("TEMPfriends.json")

	filePath = "./people/"
	data = {'key': '5C1C9CF6CAD6943D87C44DC6B3957F94',
	'steamid': str(steamid),
	'relationship': 'friend'}

	url = "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=5C1C9CF6CAD6943D87C44DC6B3957F94&steamid="+data['steamid']+"&relationship=friend"

	req = requests.get(url, data = data).text
	if req == '{}':
		print("private profile (api request returned nothing)")
		return

	with open('TEMPfriends.json', "w") as friends:
		friends.write(req)

	with open("TEMPfriends.json") as f:
		full = json.load(f)

	with open(filePath + data['steamid'] + ".json", "w") as file:
		for friend in full['friendslist']['friends']:
			# print(friend["steamid"])
			file.write(friend["steamid"] + ",\n")

	input("press enter to continue")

	if os.path.isfile("TEMPfriends.json"):
		os.remove("TEMPfriends.json")
	print("done")

getFriendList("76561198199384013")