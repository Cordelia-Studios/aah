import socket

target_host="127.0.0.1"
target_port=666

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))
client.send('JOINGAME::{"room":"unnamed", "username": "cutepussy", "groups":[ { "name": "aah", "max": 9000 } ]}'.encode())
client.close()

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))
client.send('JOINGAME::{"room":"unnamed", "username": "goodbunny" "groups":[ { "name": "aah", "max": 9000 } ]}'.encode())
client.close()

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))
client.send('PLAYCARD::{"room":"unnamed", "username": "cutepussy", "card": { "id":1, "group": "aah", "text": "My grandmother"} }'.encode())
client.close()

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))
client.send('PLAYEDCARDS::{"room": "unnamed"}'.encode())
response=client.recv(4096)
print( response )
client.close()

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))
client.send('PENDINGPLAYERS::{"room": "unnamed"}'.encode())
response=client.recv(4096)
print( response )
client.close()

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))
client.send('CHOOSECARD::{"room": "unnamed", "username": "cutepussy", "card": { "id":1, "group": "aah", "text": "My grandmother"} }'.encode())
client.close()

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))
client.send('NEWCARD::{"room": "unnamed"}'.encode())
response=client.recv(4096)
print( response )
client.close()

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))
client.send('ROUNDSTATE::{"room": "unnamed"}'.encode())
response=client.recv(4096)
print( response )
client.close()
