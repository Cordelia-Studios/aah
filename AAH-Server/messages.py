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
        game.room_id = message_data["room"]
        use_decks = message_data["decks"]
        print("Shuffling decks...")
        game.white_deck, game.black_deck = decks.shuffle(game.white_deck, game.black_deck, use_decks)
        games[Game.room_id] = game
        print("Game created")
    print("User %s is joining the room %s..." % ( message_data["username"], message_data["room"]))

    # Search for existing user
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
    return game


def startgame(message_data, games):
	game = games[message_data["room"]]
	game.choosen_player = game.players[0]
	game.phase = 0
	return game.choosen_player

def setChooser(message_data, games):
	game = games.message_data["room"]
	for i in range(len(game.players)):
		if(game.players[i]["username"]==game.choosen_player):
			game.choosen_player = game.players[(i+1)%len(game.players)]
	return game.choosen_player


def playcard( message_data, games ):
    game = games[message_data["room"]]
    print("User %s is playing %s..." % (message_data["username"], message_data["cards"] ))
    message_cards = []
    for card in message_data["cards"]:
    	message_cards.append([card["id"],card["pack"]])
    game.round_cards.append(
        {
            "player": message_data["username"],
            "cards": message_cards
        }
    )
    return None

def choosecard( message_data, games ):
    print("Choosing winner card...")
    game = games[message_data["room"]]
    message_cards = []
    for card in message_data["cards"]:
    	message_cards.append([card["id"],card["pack"]])
    game.round_winner = {
            "username": message_data["username"],
            "cards": message_cards
        }
    game.players[message_data["username"]]["score"] += 20;
    return None

def playedcards( message_data, games ):
    print("Returning played cards...")
    game = games[ message_data["room"] ]
    cards = game.round_cards
    print("Success")
    return cards

def newcard( message_data, games ):
	print("Giving new cards...")
	game = games[ message_data["room"] ]
	new_card = game.white_deck.pop()
	game.players[message_data["username"]]["hand"].append(new_card)
	game.used_white_cards.append(new_card)
	return {new_card}

def pendingplayers( message_data, games ):
    print("Returning pending players...")
    game = games[ message_data["room"] ]
    pp = len(game.players) - len(game.round_cards["cards"])
    # TO-DO: Number of pending players
    return pp

def roundstate( message_data, games ):
    print("Returning players state...")
    game = games[ message_data["room"] ]
    players = game.users
    # TO-DO: Deck played
    return players

