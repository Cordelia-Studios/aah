from game import Game
import json
import random

def joingame( dictionary , games ):
    game = games.get( dictionary["room"], False )
    if not game:
        print("Creating game %s..." % dictionary["room"] )
        game = Game
        game.room = dictionary["room"]
        game.groups = dictionary["groups"]
        games[Game.room]= game
        print("Game created")
    print("User %s is joining the room %s..." % ( dictionary["username"], dictionary["room"]))
    game.users[dictionary["username"]] = {
        "score": 0
    }
    print("Succe")
    return None

def playcard( dictionary, games ):
    game = games[dictionary["room"] ]
    print("User %s is playing %s..." % (dictionary["username"], dictionary["card"]["text"] ))
    game.deck_white.append(
        {
            "username": dictionary["username"],
            "card": dictionary["card"]
        }
    )

    return None

def choosecard( dictionary, games ):
    print("Choosing winner card...")
    game = games[dictionary["room"] ]
    game.last_winned = {
            "username": dictionary["username"],
            "card": dictionary["card"]
        }
    game.deck_white = []
    game.users[dictionary["username"]]["score"] += 20;
    return None

def playedcards( dictionary, games ):
    print("Returning played cards...")
    game = games[ dictionary["room"] ]
    cards = game.deck_white
    print("Success")
    return cards

def newcard( dictionary, games ):
    print("Getting a random card...")
    game = games[ dictionary["room"] ]
    group = random.choice( list(game.groups) )
    r1 = random.randint(1, group["max"])
    # TO-DO: Ignorar las que ya salieron
    return {"group": group["name"], "number": r1}

def pendingplayers( dictionary, games ):
    print("Returning pending players...")
    game = games[ dictionary["room"] ]
    pp = len(game.users) - len(game.deck_white)
    # TO-DO: Number of pending players
    return pp

def roundstate( dictionary, games ):
    print("Returning players state...")
    game = games[ dictionary["room"] ]
    players = game.users
    # TO-DO: Deck played
    return players
