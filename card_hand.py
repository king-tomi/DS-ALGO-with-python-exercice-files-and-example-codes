from positional_list import PositionalList

class Card:

    SUITS = [
             "C",
             "S",
             "H",
             "D"
            ]

    def __init__(self,rank: str, suit: str):
        if suit not in Card.SUITS:
            raise ValueError("this is not a correct card")
        self._rank = rank
        self._suit = suit

    def __str__(self):
        return f"{self._rank} of {self._suit}"

class CardHand:

    def __init__(self):
        self._cards = PositionalList()
        self._size = 0

    def add_card(self,r: str, s: str):
        if self._cards.is_empty():
            self._cards.add_first(s)
            self._size += 1

        if self._cards.first().element() == s:
            self._cards.add_after(self._cards.first(),s)
            self._size += 1
        elif self._cards.last().element() == s:
            self._cards.add_before(self._cards.last(),s)
            self._size += 1
        else:
            self._cards.add_last(s)
            self._size += 1

    def play(self,s: str):
        if self._cards.is_empty():
            raise ValueError("There are no more cards in hand")

        try:
            card = self._cards.delete(s)
        except ValueError:
            print(f"there is no card of suit {s} in hand, playing another card")
            avail = self._cards.delete(self._cards.first())
            return avail
        else:
            return card