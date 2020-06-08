import socket
import threading
import json
import traceback
from gameRoom import GameRoom

serverVersion = "v:0.1 Beta Dev"
bindIp="127.0.0.1"
bindPort=6000

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bindIp,bindPort))

server.listen(5)

print("AAH Server (",serverVersion,") started on",bindIp,":",bindPort)

gameRooms = {}
clients = {}


"""
TODO:
> Asincronous control
> Networking messaging component
> Full Gameplay and anti-cheating
> Save players status for reconnections

functions = {
	"STARTGAME": m.startgame,
	"JOINGAME": m.joingame,
	"PLAYCARD": m.playcard,
	"CHOOSECARD": m.choosecard,
	"PLAYEDCARDS": m.playedcards,
	"NEWCARD": m.newcard,
	"ENDGAME": m.endgame,
}
"""

def handleClient(clientSocket, clientAddress):
	print("Client Connected")
	while True:
		try:
			# Receive a request
			rawMessage = clientSocket.recv(4096).decode("utf-8")
			requestType = rawMessage.split('::')[0]
			rawData = rawMessage.split('::')[1]
			requestData = json.loads( rawData )

			if 	 requestType == "JOINGAME":
				roomName = requestData["room"]
				playerName = requestData["username"]
				responseCode, responseMessage = joingame(gameRooms, client_socket, roomName, playerName)
				if responseCode == "GOD":
					# TODO Send to all players in game the usernames
				elif responseCode == "SYN":
					# TODO Send to reconected player the game info
				elif responseCode == "RES":
					# TODO Send to player error message
			elif requestType == "ROOMOPTIONS":
			elif requestType == "STARTGAME":
			elif requestType == "PLAYCARD":
			elif requestType == "CHOOSECARD":
			elif requestType == "ENDGAME":

		except:
			# Disconnect from client and delete its socket
			# debug: 
			traceback.print_exc()
			print("Player disconected")
			for room in clients:
				for player in clients[room]:
					if clients[room][player] == client_socket:
						print("Closed ",player," Connection")
						del clients[room][player]
						break
						break
		
			client_socket.close()
			break
	"""
	while True:
		try:
			request = client_socket.recv(4096).decode("utf-8")
			print(request)
			type = request.split('::')[0]
			data = request.split('::')[1]

			print('type', type)

			message_data = json.loads( data )

			response = functions[type]( message_data, games );
			if type=="JOINGAME":
				# TODO Send data to re-connected players
				# Very artesanal "Session" control
				if message_data["room"] in clients:
					clients[message_data["room"]][message_data["username"]] = client_socket
				else:
					clients[message_data["room"]] = {message_data["username"]:client_socket}

			elif type=="STARTGAME":
				for room in clients:
					if room == response.room_id:
						# Send cards to all players
						for player in clients[room]:
							for game_player in  response.players:
								if game_player["username"] == player and player != message_data["username"]:
									#TODO send messages in new threads and improve the quality of response messages
									clients[room][player].send(str([game_player["hand"],response.round_cards["black"],response.choosen_player]).encode())
									break
							
						# Response for the player who sent START GAME
						for game_player in  response.players:
							if game_player["username"] ==  message_data["username"]:
								response = [game_player["hand"], response.round_cards["black"], response.choosen_player]
								break
						break
			
			# TODO: Easy Anti Cheat - if player plays a card that is not in his hand, re-sync the player
			elif type=="PLAYCARD":
				# Send the played cards to the chooser
				print("Players left: " + str(len(response)))
				if len(response) == 0:
					played_cards, chooser = m.playedcards(message_data, games)
					for room in clients:
						if room == message_data["room"]:
							for player in clients[room]:
								# Send cards to chooser
								if chooser == player:
									print("Sending cards to chooser (",player,")...")
									clients[room][player].send(str(played_cards).encode())
								
								# Send round status to other players
								elif message_data["username"] != player:
									#TODO send messages in new threads
									print("Sending player  (",player,") that winner is being choosen...")
									clients[room][player].send(str(len(response)).encode())		
							break
					print("Sending last player response (",message_data["username"],")...")
					response = len(response)
				else:
					# Send to the players, how many players are left to play, don't send to chooser (Its sent in response)
					chooser = games[message_data["room"]].choosen_player
					for room in clients:
						if room == message_data["room"]:
							for player in clients[room]:
									have_played = True
									for pl in response:
										if pl == player or message_data["username"] == player:
											have_played = False
											break
									if have_played:
										#TODO send messages in new threads
										print("Sending player  (",player,") how many are left...")
										clients[room][player].send(str(len(response)).encode())
					print("Sending recent player (",message_data["username"],") response...")
					response = len(response)
					
			elif type=="CHOOSECARD":
				# Send who winned the round to everyone
				chooser = message_data["username"]
				for room in clients:
					if room == message_data["room"]:
						for player in clients[room]:
							if player != chooser:
								#TODO send messages in new threads
								clients[room][player].send(str(response).encode())
						break
						
				# Reset the new round
				new_cards = m.newcard(games[message_data["room"]])
				print(new_cards)
				for room in clients:
					if room == message_data["room"]:
						for player in clients[room]:
							if player != chooser:
								player_set = {
									"white": new_cards["players"][player],
									"black": new_cards["black"],
									"chooser": new_cards["choosen"]
								}
								#TODO send messages in new threads
								clients[room][player].send(str(player_set).encode())

						response = {
							"white": [],
							"black": new_cards["black"],
							"chooser": new_cards["choosen"]
						}
						break
				print("Starting new round...")

			client_socket.send(str(response).encode())

		except:
			# Delete client socket  and close client connection
			# debug: 
			traceback.print_exc()
			print("Player disconected")
			for room in clients:
				for player in clients[room]:
					if clients[room][player] == client_socket:
						print("Closed ",player," Connection")
						del clients[room][player]
						break
						break
		
			client_socket.close()
			break
"""

def sendMessage(targetSocket, message):
	targetSocket.send(message.encode())	

def joinGame(gameRooms, socket, roomName, playerName):
	# Receives: roomName = "unnamed", playerName = "cutepussy"
	game = gameRooms.get(roomName, False)

	# Create the game room if it doesn't exists
	if not game:
		print("Creating game in room: ", roomName,"...")
		game = GameRoom
		game.roomId = roomName
		game.round = 1
		game.roundPhase == -1
		game.whiteDeck = []
		game.blackDeck = []
		game.usedWhiteCards = []
		game.usedBlackCards = []
		print("Game room succesfully created!")

	# Join the player to the game's room
	print("Player ",playerName," is joining the room ",roomName,"...")
	
	if game.roundPhase == -1: # Game not started
		inRoom = False
		for player in game.players:
			if player["username"] == playerName:
				player["socket"] = socket
				inRoom = True
				break
		if not inRoom: # New player
			game.players.append({
				"username": playerName,
		    	"hand": [],
				"score": 0,
				"socket": socket
				#TODO implement some security :
				# "cryptopass": ?
			})

		print("Player joined room ", roomName)
		# Returns all the players' nicknames
		return "GOD", game.getPlayerNames()

	else: # Game started
		inGame = False
		for player in game.players:
			if player["username"] == playerName:
				syncData = [player["hand"], game.playerScores(), game.roundCards["black"], game.roundPhase, game.round, game.roundChooser, game.playedThisRound(playerName)]
				player["socket"] = socket
				print("Player ",playerName," reconnected.")
				inGame = True
				# Returns a full game sync message for the player
				return "SYN",syncData
				break

		if not inGame:
			# Returns a negative connection type
			print("Player ",playerName," can't join to a running game, is not in room.")
			return "RES", "can't join to a running game"

while True:
	clientSocket, clientAddress = server.accept()
	clientHandler = threading.Thread(target=handleClient,args=(clientSocket,clientAddress))
	clientHandler.start()
