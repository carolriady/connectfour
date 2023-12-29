from board import Board


class Player:
    """ a data type for a Connect Four player with arbitrary dimensions
    """ 
    def __init__(self, checker):
        
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        """returns a string representing a Player object"""
        return 'Player ' + self.checker
    
    def opponent_checker(self):
        """ returns a one-character string representing the checker of 
        the Player object’s opponent"""
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
        
    def next_move(self, b):
        """ accepts a Board object b as a parameter and returns the column 
        where the player wants to make the next move."""
        self.num_moves += 1
        while True:   
            col = int(input("Enter a column: "))
            if col < b.width and col > 0:
                return col
            else:
                print('Try again!')