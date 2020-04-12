list1 = ["a","a","a"]
list2 = list1.copy()
list2.pop()
print(list1,list2)


"""
import socket

target_host="127.0.0.1"
target_port=670

origin_host="127.0.0.1"
origin_port=671

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))
print("Joining game...")
client.send('JOINGAME::{"room":"unnamed", "username": "goodbunny", "decks":["BASE"]}'.encode())
print(client.recv(4096).decode("utf-8"))
print(client.recv(4096).decode("utf-8"))
while True:
	message = input("Code?")
	if message == "1":
		client.send('STARTGAME::{"room":"unnamed", "username": "cutepussy", "decks":["BASE"]}'.encode())
		print(client.recv(4096).decode("utf-8"))

	elif message == "2":
		client.send('JOINGAME::{"room":"unnamed", "username": "cutepussy", "decks":["BASE"]}'.encode())
		print(client.recv(4096).decode("utf-8"))

	elif message == "3":
		print(client.recv(4096).decode("utf-8"))


client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))
print("Joining game...")
client.send('STARTGAME::{"room":"unnamed"}'.encode())
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
