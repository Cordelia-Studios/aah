import socket
import threading
import messages as m
import json

bind_ip="127.0.0.1"
bind_port=669

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print("I'm  listening on %s on the port %d" % (bind_ip,bind_port))

games = {}

functions = {
    "GAMEINFO": m.gameinfo,
    "PLAYCARD": m.playcard,
    "CHOOSECARD": m.choosecard,
    "JOINGAME": m.joingame,
    "PLAYEDCARDS": m.playedcards,
    "NEWCARD": m.newcard,
    "PENDINGPLAYERS": m.pendingplayers,
    "PLAYERSSTATE": m.playersstate,
}

def handle_client(client_socket):
    request = client_socket.recv(4096).decode("utf-8")
    type = request.split('::')[0]
    data = request.split('::')[1]

    print('type', type)

    dictionary = json.loads( data )

    response = functions[type]( dictionary, games );
    client_socket.send(str(response).encode())

    client_socket.close()

while True:
	client, addr = server.accept()
	client_handler = threading.Thread(target=handle_client,args=(client,))
	client_handler.start()
