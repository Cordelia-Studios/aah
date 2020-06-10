# App Against Humanity
## Clientes:
Solo existe un cliente actualmente, funciona para linea de comandos, hecho en python.
## Server-Side

### Mensajes de Cliente a Servidor:
Todos los mensajes se envían y se reciben en formato Json a traves de sockets

**JoinGame:** 
Crea salas y une jugadores 
- Recibe:
	- Nombre de sala
	- Nombre de jugador
- Responde:
	- Si el juego no ha iniciado, Lista de jugadores en la sala.
	- Si el juego ya ha iniciado y estaba en la sala, Mensaje de sincronización con los datos del juego en curso.
	- Si el juego ya ha iniciado y no estaba en la sala, Mensaje de error.

**RoomOptions:**
- Recibe:
	- Nombre de sala
	- Nombre de jugador
	- Mazos a usar
	- Numero de rondas máximas
	- Tamaño de la sala
- Responde:
	- Verificación booleana de las opciones dadas

**KickPlayer:**
- Recibe:
	- Nombre de sala
	- Nombre de jugador
	- Nombre de jugador a expulsar
- Responde:
	- Verificación de la expulsión

**TransferOwner:**
- Recibe:
	- Nombre de sala
	- Nombre de jugador
	- Nombre de nuevo dueño de la sala
- Responde:
	- Verificación de la transferencia

**ExitGame:**
- Recibe:
	- Nombre de sala
	- Nombre de jugador
- Responde:
	- Verificación de salida de sala

**StartGame:**
- Recibe:
	- Nombre de sala
	- Nombre de jugador
- Responde:
	- Inicia el juego de la sala, si no ha iniciado ya.

**PlayCard:**
- Recibe:
	- Nombre de sala
	- Nombre de jugador
	- Cartas jugadas para el turno
- Responde:
	- Lista de jugadores restantes por jugar.

**ChooseCard:**
- Recibe:
	- Nombre de una sala
	- Nombre de jugador
	- Nombre de jugdaor ganador de la ronda.
- Responde:
	- Envía a cada jugador cartas blancas nuevas, una nueva carta negra, y el nombre del jugador que elegirá el ganador de esta ronda.

**EndGame:**
- Recibe:
	- Este mensaje no se envía al servidor
- Responde:
	- A cada jugador se le envía la puntuación final del juego y los desconecta de la sala.

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


### Funcionamiento del servidor:
El servidor maneja envío de mensajes por sockets de manera asíncrona intentando minimizar los datos enviados y recibidos de los jugadores.

El servidor almacena los datos de los juegos en salas, donde cada sala tiene un único juego en curso.

**Datos del juego:**
- Nombre de sala
- Mazos Utilizados
- Ronda
- Fase de la ronda
- Rondas Máximas
- Numero de Jugadores Máximo
- Mazo negro
- Mazo blanco
- Mazo de cartas desechadas
- Jugadores
	- Username
	- Cartas en mano
	- Puntaje
	- Conexión con servidor
- Jugador de selección de ronda
- Jugadores restantes por jugar
  

(Todas las cartas se manejan con un ID)