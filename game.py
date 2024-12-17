from card import Card

from ursina import *
import random

deck = [
    "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "TC", "JC", "QC", "KC",
    "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "TD", "JD", "QD", "KD",
    "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "TH", "JH", "QH", "KH",
    "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "TS", "JS", "QS", "KS"
]

if __name__ == '__main__':
    application.development_mode = False

    app = Ursina()
    window.size = (1152, 720)

    card = Card("AC", True, Vec2(0.5, 0.5))

    app.run()



class Card():
    def __init__(self, value: str, is_face_up: bool):
        self.is_face_up = is_face_up# Whether the card is face up or face down
        self.value = value
        
    def flip_card(self):
        self.is_face_up = not self.is_face_up


class Dealer():
    def __init__(self, deck_count: int):
        self.shoebox = [] 
        self.hand = []
        
        temp = []
        for x in range(deck_count):
            temp.append(deck)

        for sub_list in temp:
            for value in sub_list:
                card = Card(value, True)            
                self.shoebox.append(card)

        # Shuffle Showbox
        random.shuffle(self.shoebox)

    def deal_card(self) -> str:
        return self.shoebox.pop()


def is_bust(c1: Card, c2: Card) -> bool:
    if c1 + c2 > 21:
        return True
    else:
        return False