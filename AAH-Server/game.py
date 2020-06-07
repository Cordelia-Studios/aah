class Game:
	room_id = ""
	players = [
	    # {
	    #	  username": "Paco"
	    #	  "hand": [["aahW",85],["aahW",5],...]
		#	  "score": 0
	    # }
	]

	round_phase = -1 # -1 - Non started game / 0 - White cards play Phase / 1 - Choose winner phase 
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
	    # "black": ["pack",#id]
	}

	round_cards = {
		# "cards": [
		#	["username",["aahW",56],["aahW",57]],
		#	["Paco    ",["aahW",65],["aahW",66]]
		#]
		# "black": ["aahB",20,2]
	}

	left_players = []

	choosen_player = ""

	def __str__(self):
		data = "room id:" + room_id + "\nplayers" + players + "\nround" + round_cards
		
		return data




