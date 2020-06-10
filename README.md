# App Against Humanity
## Clientes:
Solo existe un cliente actualmente, funciona para linea de comandos, hecho en python.
## Server-Side

### Mensajes de Cliente a Servidor:
Todos los mensajes se envían y se reciben en formato Json a traves de sockets

**JoinGame:** 
Crea salas y une jugadores 
- Recibe:
	- Nombre de una sala
	- Nombre de jugador
- Responde:
	- Si el juego no ha iniciado, Lista de jugadores en la sala.
	- Si el juego ya ha iniciado y estaba en la sala, Mensaje de sincronización con los datos del juego en curso.
	- Si el juego ya ha iniciado y no estaba en la sala, Mensaje de error.

**RoomOptions:**
- Recibe:
	- Nombre de una sala
	- Nombre de jugador
- Responde:
	- Si el juego no ha iniciado, Lista de jugadores en la sala.
	- Si el juego ya ha iniciado y estaba en la sala, Mensaje de sincronización con los datos del juego en curso.
	- Si el juego ya ha iniciado y no estaba en la sala, Mensaje de error.

KickPlayer:
- Recibe:
	- Nombre de una sala
	- Nombre de jugador
- Responde:
	- Si el juego no ha iniciado, Lista de jugadores en la sala.
	- Si el juego ya ha iniciado y estaba en la sala, Mensaje de sincronización con los datos del juego en curso.
	- Si el juego ya ha iniciado y no estaba en la sala, Mensaje de error.

TransferOwner:
- Recibe:
	- Nombre de una sala
	- Nombre de jugador
- Responde:
	- Si el juego no ha iniciado, Lista de jugadores en la sala.
	- Si el juego ya ha iniciado y estaba en la sala, Mensaje de sincronización con los datos del juego en curso.
	- Si el juego ya ha iniciado y no estaba en la sala, Mensaje de error.

ExitGame:
StartGame:
PlayCard:
ChooseCard:
EndGame:


### Servidor a Cliente
PlayedCards:
Va a un jugador tipo 1 cuando pasa se pasa a segunda fase de ronda.
- n x Id Carta (n - numero de jugadores)

NewCard:
Va a cada jugador tipo 0 al iniciar ronda.
- Id carta
- Id carta pregunta - Se envia también solo esta carta al jugador tipo 1

RoundWinner:
Va a todos los jugadores:
- Id jugador ganador
- Id carta gandora

Wait:
Va a todo jugador tipo 0 que ya haya jugado esta ronda.
- Numero de jugadores restantes por jugar

SyncErr:
Va a un jugador que envie datos erroneos:
- Id Cartas de jugador
- Puntajes


## Datos:
- Juego Activo:
    - Cartas en Deck Respuesta
    - Cartas en Deck Juego
    - Jugadores
        - Id Jugador
        - Cartas
        - Puntaje
        - Rol de ronda (0 - Juega su carta/1 - Escoge al ganador)
    - Id Juego
    - Numero de ronda
    - Estado ronda
        - Fase (Elegir cartas/Elegir ganador)
        - Cartas en juego

(Todas las cartas se manejan con un ID)