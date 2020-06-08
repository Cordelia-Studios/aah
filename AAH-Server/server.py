import socket
import threading
import messages as m
import json
import traceback

serverVersion = "v:1.0 Alpha Dev"
bind_ip="127.0.0.1"
bind_port=6000

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print("I'm  listening on %s on the port %d" % (bind_ip,bind_port))

games = {}
# Have the actual socket of each player in each game room
clients = {}

functions = {
	"STARTGAME": m.startgame,
	"JOINGAME": m.joingame,
	"PLAYCARD": m.playcard,
	"CHOOSECARD": m.choosecard,
	"PLAYEDCARDS": m.playedcards,
	"NEWCARD": m.newcard,
	"ENDGAME": m.endgame,
}

def handle_client(client_socket):
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

while True:
	client, addr = server.accept()
	client_handler = threading.Thread(target=handle_client,args=(client,))
	client_handler.start()

# TO DO Set a game end condition
# TO DO Low level Anti cheat by server data copies