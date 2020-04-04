# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 21:27:31 2020

@author: Karol
"""


class Board(object):
    """
    
    Board where fourinarow will take place 
    
    
    """
    
    board_state = []
    
    def __init__(self, row=6, column=7):
        """Returns board object with row number and column number"""
        self.row = row
        self.column = column
        for row_no in range(row):
            row = []
            for column_no in range(column):
                row.append(0)
            self.board_state.append(row)
        
    
    
    def show_board(self):
        """Prints board into console"""
        for row in self.board_state:
            print(row)
                
    
    def update_board(self, player_marker, column):   
        """Updates board_state with marker in place specified"""
        for count, i in enumerate(reversed(self.board_state)):
            if i[column] != 0:
                pass
            elif i[column] == 0:
                row_upd=5-count
                break
            else:
                row_upd=5
                break
        self.board_state[row_upd][column] = player_marker
        
        
    
    
        