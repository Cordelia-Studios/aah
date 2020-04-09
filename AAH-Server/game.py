class Game:
	room_id = ""
	players = [
	    # {
	    #	  username": "Paco"
	    #	  "hand": [["aahW",85],["aahW",5],...]
		#	  "score": 0
		#	  "socket": player socket
	    # }
	]

	round_phase = -1
	round = 1

	black_deck = [
		# ids ->  ["aahW",56,#Whites], ["aahW",1,#Whites]
	]

	white_deck = [
		# ids ->  ["aahB",56], ["aahB",1]
	]

	used_white_cards = [
	    # poped white card ids
	]

	used_black_cards = [
	    # poped black card ids
	]

	round_winner = {
	    # "username": "username",
	    # "cards" : [["pack",#id],["pack",#id]]
	}

	round_cards = [
		# {
		# "player": "playerId"
		# "cards": [["aahW",56],["aahW",56]]
		# "black": ["aahB",20]
		# }
	]

	choosen_player = ""




