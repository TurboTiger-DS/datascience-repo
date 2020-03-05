# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 21:17:46 2020

@author: Karol
"""

"""

Plansza 6x7

"""

from board import Board

GameBoard = Board()
GameBoard.show_board()

print("Teraz nastąpi ruch")

GameBoard.update_board(1, 2, 2)
GameBoard.show_board()



