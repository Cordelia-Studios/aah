from game import Game
import decks
import json
import random


def joingame( message_data , games ):
	game = games.get( message_data["room"], False )

	# Create new game if room doesn't exists
	if not game:
		print("Creating game %s..." % message_data["room"] )
		game = Game
		game.round=1
		game.room_id = message_data["room"]
		use_decks = message_data["decks"]
		print("Shuffling decks...")
		game.white_deck, game.black_deck = decks.shuffle(game.white_deck, game.black_deck, use_decks)
		games[Game.room_id] = game
		print("Game created")
	print("User %s is joining the room %s..." % ( message_data["username"], message_data["room"]))

	# Search for existing user
	# TO Do: if a player re-connects send the actual game data, cases: Game not started, Pre-whites, 
	existing = False
	for player in game.players:
		if player["username"] == message_data["username"]:
			existing = True
			break
	if not existing:
		game.players.append({
			"username": message_data["username"],
			"hand": [],
			"score": 0
		})
	print("Success")
	return len(game.players)


def startgame(message_data, games):
	game = games[message_data["room"]]
	for player in game.players:
		for i in range(10):
			whiteCard = game.white_deck.pop()
			player["hand"].append(whiteCard)
			game.used_white_cards.append(whiteCard)
	game.choosen_player = game.players[0]["username"]
	blackCard = game.black_deck.pop()
	game.round_cards["cards"] = []
	game.round_cards["black"] = blackCard
	game.used_black_cards.append(blackCard)
	game.phase = 0
	game.left_players = []
	for i in range(1,len(game.players)):
		game.left_players.append(game.players[i]["username"]) 
	return game

def playcard( message_data, games ):
	game = games[message_data["room"]]
	print("User %s is playing %s..." % (message_data["username"], message_data["cards"] ))
	game.round_cards["cards"].append([message_data["username"],message_data["cards"]])
	game.left_players.remove(message_data["username"])
	# Delete cards from hand in server
	for player in game.players:
		if player["username"] == message_data["username"]:
			for hand_card in message_data["cards"]:
				player["hand"].remove(hand_card)
			break
	if len(game.left_players) == 0:
		game.round_phase = 1
	return game.left_players.copy()

def playedcards( message_data, games ):
	game = games[ message_data["room"] ]
	cards = game.round_cards
	choosen = game.choosen_player
	return cards, choosen

def choosecard( message_data, games ):
	game = games[message_data["room"]]
	print("Choosing winner card...")
	for round_player in game.round_cards["cards"]:
		if round_player[0] == message_data["winner"]:
			for player in game.players:
				if player["username"] == message_data["winner"]:
					game.round_winner["username"] = player["username"]
					game.round_winner["cards"] = []
					game.round_winner["black"] = game.round_cards["black"]
					for i in range(1,len(round_player)):
						game.round_winner["cards"].append(round_player[i])
					player["score"] += 20
					return game.round_winner

# Error here
def newcard(game):
	print("Giving new cards...")
	new_round = {"players":{}}
	for player in game.players:
		new_round["players"][player["username"]] = []
		while len(player["hand"]) < 10:
			print(player["hand"])
			whiteCard = game.white_deck.pop()
			player["hand"].append(whiteCard)
			game.used_white_cards.append(whiteCard)
			new_round["players"][player["username"]].append(whiteCard)
	blackCard = game.black_deck.pop()
	game.used_black_cards.append(blackCard)
	new_round["black"] = blackCard
	new_round["choosen"] = setChooser(game)
	game.round += 1
	game.round_phase = 0
	game.round_cards["cards"] = []
	game.round_cards["black"] = blackCard
	game.left_players = []
	for i in range(len(game.players)):
		if game.players[i]["username"] != new_round["choosen"]:
			game.left_players.append(game.players[i]["username"]) 
	return new_round 

def setChooser(game):
	for i in range(len(game.players)):
		if(game.players[i]["username"]==game.choosen_player):
			game.choosen_player = game.players[(i+1)%len(game.players)]["username"]
			return game.choosen_player 
			
def endgame( message_data, games):
	do_something = False


