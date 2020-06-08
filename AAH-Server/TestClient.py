import socket
import json
import sys

# BIG TODO - on message receive, use 2 types, NPM (No problem Message) / SYN (Data Corrupted, re-syncing player)

def receive(client):
	raw = client.recv(4096).decode("utf-8")
	#print(raw)
	filtered = json.loads(raw.replace("'", '"'))
	return filtered

def selectUsername():
	defUsernames = ["Slifer", "cutepussy", "goodbunny"]
	for i in range(len(defUsernames)):
		print(i+1, ". ", defUsernames[i])
	selection = int(input("> "))
	return defUsernames[selection-1]


def mainMenu(owner):
	if(not owner):
		print("1. Join Game")
	if (owner):
		print("2. Start Game")
	print("3. Exit Ctrl+C")
	selection = int(input("> "))
	return selection

def playMenu():
	print("1. Play White Card")
	print("2. See Scores")
	print("3. Exit Ctrl+C")
	selection = int(input("> "))
	return selection

def playCard(hand,roundBlackCard):
	print("Play ", roundBlackCard[2]," cards:")
	cards = []
	for card in range(roundBlackCard[2]):
		for i in range(len(hand)):
			print(i+1, ". ", hand[i])
		selection = int(input("> "))
		cards.append(hand.pop(selection-1))
	return cards

def chosCard(whiteCards, blackCard):
	print("Choose winner card:")
	for i in range(len(whiteCards)):
		print(i+1,". ",end="")
		for k in range(blackCard[2]):
			print(whiteCards[i][1][k],end=", ")
		print()
	selection = int(input("> "))-1
	return whiteCards[selection][0]

# Network config
target_host="127.0.0.1"
target_port=6000

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((target_host,target_port))

# Player and Game Config
username = selectUsername();
roomName = "Room 1"
decks = '["BASE"]'
hand = []
roundBlackCard = []
roundCards = []
chooser = False
scores = {username: 0}
owner = False
ownerName = ""
roundPhase = -1
nPlayers = 0

selection = 3;
while(selection == 3 or (owner and selection != 2)):
	selection = mainMenu(owner)
	if(selection == 1): #Join Game
		print("Joining game as ", username, "...")
		message = 'JOINGAME::{"room":"'+roomName+'", "username": "'+username+'", "decks":'+decks+'}'
		clientSocket.send(message.encode())
		response = receive(clientSocket)
		if response == 1:
			owner = True
			print("Joined to game room "+roomName+" as Room Master")
		else:
			print("Joined to room "+roomName)
			print("Waiting game to start")
			response = receive(clientSocket)
			hand = response[0]
			roundBlackCard = response[1]
			chooserName = response[2]
			if chooserName == username: chooser = True
			roundPhase = 0
			print("Hand: ",len(hand)," White Cards")
			print("Black card: ",roundBlackCard)
			print("Choosing card: ",chooser,", ",response[2])

	elif(selection == 2): #Start Game
		if owner:
			print("Starting game "+roomName)
			message = 'STARTGAME::{"room":"'+roomName+'", "username": "'+username+'"}'
			clientSocket.send(message.encode())
			response = receive(clientSocket)
			hand = response[0]
			roundBlackCard = response[1]
			chooserName = response[2]
			if chooserName == username: chooser = True
			roundPhase = 0
			print("Hand: ",len(hand)," White Cards")
			print("Black card: ",roundBlackCard)
			print("Choosing card: ",chooser,", ",response[2])
		else:
			print("Only the Room Master, our lord and ruler can start the game")
			

	elif(selection == 3): #Exit Game
		clientSocket.close()
		print("Nice, Go away, and never come back")
		sys.exit(0)

while(selection != 9):
	if(chooser):
		roundCards = receive(clientSocket)
		while (not isinstance(roundCards,dict)):
			roundCards = receive(clientSocket)
			print(roundCards, " players left")
		winner = chosCard(roundCards["cards"], roundCards["black"])
		message = 'CHOOSECARD::{"room":"'+roomName+'", "username": "'+username+'", "winner":"'+winner+'"}'
		message = message.replace("'", '"')
		clientSocket.send(message.encode())
		chooser = False
		newCards = receive(clientSocket)
		roundBlackCard = newCards["black"]
		chooserName = newCards["chooser"]
	else:
		selection = playMenu();
		if(selection == 1): # Play Card
			cards = playCard(hand, roundBlackCard)
			message = 'PLAYCARD::{"room":"'+roomName+'", "username": "'+username+'", "cards":'+str(cards)+'}'
			message = message.replace("'", '"')
			clientSocket.send(message.encode())

			# Wait for all players
			leftPlayers = receive(clientSocket)
			while(leftPlayers < 0):
				print(leftPlayers, " players left.")
				leftPlayers = receive(clientSocket)

			print(chooserName," is choosing the winner.")
			roundWinner = receive(clientSocket)
			if roundWinner["username"] == username:
				print("You winned the round!")
			else:
				print(roundWinner["username"]+" winned the round.")
			scores[roundWinner["username"]] +=1

			newCards = receive(clientSocket) # Da cartas blancas nuevas, la carta negra y quien escoge la siguiente ronda
			hand.extend(newCards["white"])
			roundBlackCard = newCards["black"]
			chooserName = newCards["chooser"]
			if(chooserName == username): chooser = True

		elif(selection == 2): # See Scores
			print(scores)
		elif(selection == 9):
			sys.exit(0)

	

"""
print("Joining game...")
client.send('JOINGAME::{"room":"unnamed", "username": "goodbunny", "decks":["BASE"]}'.encode())
print(client.recv(4096).decode("utf-8"))
while True:
	message = input("Code?")
	if message == "1":
		client.send('JOINGAME::{"room":"unnamed", "username": "cutepussy", "decks":["BASE"]}'.encode())
		print(client.recv(4096).decode("utf-8"))


	elif message == "2":
		client.send('STARTGAME::{"room":"unnamed", "username": "goodbunny"}'.encode())
		data = receive(client)
		myhand = data[0]
		blackhawk = data[1]
		pickle = data[2]
		print("Za Hando: ",myhand,"\n Black Card: ",blackhawk,"\n Whos picking: ",pickle)
		data = receive(client)
		print("lefts: "+str(data))

	elif message == "3":
		newsend = str(myhand[:blackhawk[2]]).replace("'",'"')
		client.send('PLAYCARD::{"room":"unnamed", "username": "goodbunny", "cards":' + newsend + '}'.encode())
		print(receive(client))

	elif message == "5":
		client.send('CHOOSECARD::{"room":"unnamed", "username": "goodbunny", "winner":"cutepussy"}'.encode())
		print(client.recv(4096).decode("utf-8"))

	elif message == "10":
		print(client.recv(4096).decode("utf-8"))

	elif message == "11":
		client.close()
###########################################################################################################################################

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))
print("Playing card...")
client.send('PLAYCARD::{"room":"unnamed", "username": "cutepussy", "cards": [{ "id":1, "pack": "aahW"}] }'.encode())
client.close()

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))
print("Getting played cards...")
client.send('PLAYEDCARDS::{"room": "unnamed"}'.encode())
response=client.recv(4096)
print( response )
client.close()

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))
print("Getting pending players...")
client.send('PENDINGPLAYERS::{"room": "unnamed"}'.encode())
response=client.recv(4096)
print( response )
client.close()

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))
print("Chosing winner card...")
client.send('CHOOSECARD::{"room": "unnamed", "username": "cutepussy", "card": { "id":1, "group": "aah", "text": "My grandmother"} }'.encode())
client.close()

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))
print("Getting card from deck...")
client.send('NEWCARD::{"room": "unnamed"}'.encode())
response=client.recv(4096)
print( response )
client.close()

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))
print("Getting round state...")
client.send('ROUNDSTATE::{"room": "unnamed"}'.encode())
response=client.recv(4096)
print( response )
client.close()
"""