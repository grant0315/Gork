from ursina import *
from direct.stdpy import thread # We need threading to load entities in the background
import random


if __name__ == '__main__':
    application.development_mode = True

    window.title = "Gork"

    app = Ursina()

    # init startin vars
    player_hand, house_hand = []
    dealer = Dealer(4)

    # 
    app.run()
