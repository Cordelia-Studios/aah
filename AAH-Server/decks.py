import random

DECKS={
	"BASE": ["aah",500,80],
	"BASEBLACK": [1,1,1,1,1,2,1,2,2,1,1,2,1,1,2,1,1,1,1,3,1,1,1,2,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,3,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,2,1,1,1,1] 
}

def shuffle(white_deck, black_deck, use_decks):
	for name in use_decks:
		for i in range(DECKS[name][1]):
			white_deck.append([DECKS[name][0]+"W",i])
		for i in range(DECKS[name][2]):
			black_deck.append([DECKS[name][0]+"B",i,DECKS[name+"BLACK"][i]])

	random.shuffle(white_deck)
	random.shuffle(black_deck)
	return white_deck, black_deck


