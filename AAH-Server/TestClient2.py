import socket
import json

def receive(client):
	raw = client.recv(4096).decode("utf-8")
	#print(raw)
	filtered = json.loads(raw.replace("'", '"'))
	return filtered

def gethando(client,h,b,p):
	data = receive(client)
	h = data[0]
	b = data[1]
	p = data[2]
	print("Za Hando: ",myhand,"\n Black Card: ",blackhawk,"\n Whos picking: ",pickle)

def mainMenu():
	print("1. Join Game")
	print("2. Start Game")
	print("3. Exit Ctrl+C")
	selection = int(input("> "))
	return selection;

# Network config
target_host="127.0.0.1"
target_port=6000

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((target_host,target_port))

# Player and Game Config
username = "Cutepussy"
roomName = "Room 1"
decks = '["BASE"]'
hand = []
roundBlackCard = []
chooser = False
scores = {username: 0}
owner = False
roundPhase = -1


selection = 1;
while(selection == 1):
	selection = mainMenu()
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

	elif(selection == 2): #Start Game
		if owner:
			print("Starting game "+roomName)
			message = 'STARTGAME::{"room":"'+roomName+'", "username": "'+username+'"}'
			clientSocket.send(message.encode())
			response = receive(clientSocket)
			hand = response[0]
			roundBlackCard = response[1]
			if response[2] == username: chooser = True
			roundPhase = 0
			print("Hand: ",len(hand)," White Cards")
			print("Black card: ",roundBlackCard)
			print("Choosing card: ",chooser,", ",response[2])
		else:
			print("Only the Room Master, our lord and ruler can start the game")
			print("Waiting game to start")
			print(receive(clientSocket))

	elif(selection == 3): #Exit Game
		clientSocket.close()
		print("Nice, Go away, and never come back")

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