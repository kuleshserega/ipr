from collections import namedtuple
from random import choice


Card = namedtuple('Card', ('rank', 'suit'))


class CardDeck:
	ranks = [str(n) for n in range(2, 11) + list('JDKA')]
	suits = 'spades diamonds clubs hearts'.split()

	def __init__(self):
		self._cards = [
			Card(suit, rank) for suit in self.suits for rank in self.ranks
		]

	def __getitem__(self, position):
		return self._cards[position]

	def __len__(self):
		return len(self._cards)


if __name__ == '__main__':
	deck = CardDeck()
	print(choice(deck))
	print(deck[2])
