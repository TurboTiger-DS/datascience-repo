# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 21:17:46 2020

@author: Karol
"""

"""

Plansza 6x7

"""
import time

def StartGame(board, play=True):
    turn = 0
    
    input('4 in a Row. Click ENTER to start: ')
    
    while play:
        
        
        move = int(input('Which column? '))-1
        board.update_board(1, move)
        turn += 1
        board.show_board()
        
        if turn>=3:
            play=False

