import socket
import threading
import messages as m
import json
import traceback

bind_ip="127.0.0.1"
bind_port=670

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print("I'm  listening on %s on the port %d" % (bind_ip,bind_port))

games = {}
clients = {}

functions = {
    "STARTGAME": m.startgame,
    "PLAYCARD": m.playcard,
    "CHOOSECARD": m.choosecard,
    "JOINGAME": m.joingame,
    "PLAYEDCARDS": m.playedcards,
    "NEWCARD": m.newcard,
    "PENDINGPLAYERS": m.pendingplayers,
    "ROUNDSTATE": m.roundstate,
}

def handle_client(client_socket):
	while True:
		try:
			request = client_socket.recv(4096).decode("utf-8")
			type = request.split('::')[0]
			data = request.split('::')[1]

			print('type', type)

			message_data = json.loads( data )

			response = functions[type]( message_data, games );
			if type=="JOINGAME":
				if response.room_id in clients:
					clients[response.room_id][message_data["username"]] = client_socket
				else:
					clients[response.room_id] = {message_data["username"]:client_socket}
			client_socket.send(str(response).encode())

		except:
			# Delete and close client connection
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

