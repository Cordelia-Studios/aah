class GameRoom:

	roomId = ""
	players = [
		#{
	    #		"username": "Paco",
	    #		"hand": [["aahW",85],["aahW",5],...],
		#		"score": 0,
		#		"socket": clientSocket,
		#		"cryptopass": ?
		#}
		]

	roundPhase = -1 # -1 - Non started game / 0 - White cards play Phase / 1 - Choose winner phase 
	
	round = 1

	maxRound = 20

	roundChooser = ""
	
	blackDeck = [
		# ids ->  ["aahW",56,#Whites], ["aahW",1,#Whites]
	]
	whiteDeck = [
		# ids ->  ["aahB",56], ["aahB",1]
	]
	usedWhiteCards = [
	    # poped white card ids
	    # ids ->  ["aahB",56], ["aahB",1]
	]
	usedBlackCards = [
	    # poped black card ids
	    # ids ->  ["aahW",56,#Whites], ["aahW",1,#Whites]
	]

	roundWinner = {
	    # "username": "username",
	    # "cards" : [["pack",#id],["pack",#id]]
	    # "black": ["pack",#id]
	}

	roundCards = {
		# "plays": [
		#	["username",["aahW",56],["aahW",57]],
		#	["Paco    ",["aahW",65],["aahW",66]]
		#]
		# "black": ["aahB",20,2]
	}

	leftPlayers = [
		# "John", "Paco", "BadOnes"
	]


	def getPlayerNames():
		players = []
		for player in players:
			players.append(player["username"].copy())
		return players

	def getPlayerScores():
		playerScores = {}
		for player in players:
			playerScores[player["username"]] = player["score"].copy()
		return playerScores

	def playedthisRound(username):
		if username == roundChooser:
			return False
		for player in leftPlayers:
			if username == player:
				return  = False
		return True