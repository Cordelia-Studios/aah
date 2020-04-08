<h2 align="center">Messages</h2>

### JOINGAME

> Starts the game if the room doesn't exist or join the room if it does

#### Request

- room: Name of the room.
- username: Username of the player.
- groups: List of groups of cards.
  - name: Name of the group of cards.
  - max: Size of the group.

#### Response

None

#### PLAYCARD

> Plays the card

#### Request

- room: Name of the room.
- username: Username of the player.
- card: Card played.
  - id: Id of the card, equals to the number of line in the file.
  - group: Name of the group, equals to the name of the file.
  - text: Text of the card.

#### Response

None

#### CHOOSECARD

> Player choses the winner

#### Request

- room: Name of the room.
- username: Username of the player.
- card: Card played.
  - id: Id of the card, equals to the number of line in the file.
  - group: Name of the group, equals to the name of the file.
  - text: Text of the card.

#### Response

None

#### PLAYEDCARDS
> Goes to every player on the second stage.

#### Request

- room: Name of the room.

#### Response

- cards: List of cards played.
  - id: Id of the card, equals to the number of line in the file.
  - group: Name of the group, equals to the name of the file.
  - text: Text of the card.

#### NEWCARD

> Goes to every type 0 player when starting round.

#### Request

- room: Name of the room.

#### Response

- group: Group's name, equals to the name of the file.
- number: Random number, equals to the number of the line.


#### PENDINGPLAYERS

> It's sent everu time a player plays.

#### Request

- room: Name of the room.

#### Response

- players: Number of pending players.

#### ROUNDSTATE

> It's sent every time a round ends.

#### Request

- room: Name of the room.

#### Response

- cards: List of cards played.
  - username: Username of the player.
  - score: Score of the player.
  - card: Card played.
    - id: Id of the card, equals to the number of line in the file.
    - group: Name of the group, equals to the name of the file.
    - text: Text of the card.


<h2 align="center">Data</h2>

### On the server

- room: Name of the room
- Cartas en Deck Respuesta
- Cartas en Deck Juego
- player
    - username
    - cards
    - score
    - rol (0 - is playing/1 - is selecting the winner)
- round: Number of the round
- state: State of the game
    - stage: 0 if selecting cards, 1 if choosing the winner
    - cards: List of cards

### On the client

- deck
- rol
- turn
- scores
- stage
