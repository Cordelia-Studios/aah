def chosCard(whiteCards, blackCard):
	print(whiteCards)
	print("Choose winner card:")
	for i in range(len(whiteCards)):
		print(i+1,". ",end="")
		for k in range(blackCard[2]):
			print("i: ",i,", k:",k)
			print(whiteCards[i][1][k],end=", ")
		print()
	selection = int(input("> "))-1
	return whiteCards[selection][0]


a = {"cards": [['cutepussy', [['aahW', 258], ['aahW', 374]]]],
	 "black": ["aahB",20,2]}
if isinstance(a,dict):
	print(chosCard(a["cards"],a["black"]))
else:
	print("not dict, is a ", type(a))



"""
import socket
import json

def receive(client):
	raw = client.recv(4096).decode("utf-8")
	filtered = json.loads(raw.replace("'", '"'))
	return filtered

def gethando(client,h,b,p):
	data = receive(client)
	h = data[0]
	b = data[1]
	p = data[2]
	print("Za Hando: ",h,"\n Black Card: ",b,"\n Whos picking: ",p)
	return h,b,p

target_host="127.0.0.1"
target_port=6000

origin_host="127.0.0.1"
origin_port=6000

myhand = []
blackhawk = []
pickle = ""


client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))
print("cutepussy is Joining game...")
client.send('JOINGAME::{"room":"unnamed", "username": "cutepussy", "decks":["BASE"]}'.encode())
print(client.recv(4096).decode("utf-8"))
myhand,blackhawk,pickle = gethando(client,myhand,blackhawk,pickle)
while True:
	message = input("Code?")
	if message == "1":
		client.send('JOINGAME::{"room":"unnamed", "username": "goodbunny", "decks":["BASE"]}'.encode())
		rawData = client.recv(4096).decode("utf-8")
		print(rawData)

	elif message == "2":
		client.send('STARTGAME::{"room":"unnamed", "username": "cutepussy"}'.encode())
		data = receive(client)
		myhand = data[0]
		blackhawk = data[1]
		pickle = data[2]
		print("Za Hando: ",myhand,"\n Black Card: ",blackhawk,"\n Whos picking: ",pickle)

	elif message == "3":
		newsend = str(myhand[:blackhawk[2]])
		sendStr = 'PLAYCARD::{"room":"unnamed", "username": "cutepussy", "cards":'+newsend+'}'
		client.send(str(sendStr).replace("'",'"').encode())
		data = receive(client)
		print(data)

	elif message == "5":
		client.send('CHOOSECARD::{"room":"unnamed", "username": "cutepussy", "winner":"goodbunny"}'.encode())
		print(client.recv(4096).decode("utf-8"))

	elif message == "10":
		print(receive(client))

	elif message == "11":
		client.close()
 



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
while True:
	0 == 0