# steamWebApiFriends
using steam web api to find users friends list

Finds how you are linked to ~400k other users who are friends of friends, or further

To use run Run.py and select one of the options

getDataAndWrite - gets friends lists from steam and creates json file
- you need to run this at least once before using the rest of the program
- requires you to input your steam api key to use the steam api to get friends lists
- accepts steam id as the initial user (who to generate tree from)
- creates json file with all steam ids
- if json file already exists, it gets replaced

findUser - finds the path from input user to origin of input file
- accepts steam id to find path to
- prints path found
