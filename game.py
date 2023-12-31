#
#
# Playing the game 
#   

from board import Board
from player import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b
        
def process_move(p, b):
    """takes two parameters: a Player object p for the player whose move 
    is being processed, and a Board object b for the board on which the 
    game is being played."""
    print(str(p)+ "'s turn")
    move1 = p.next_move(b)
    b.add_checker(p.checker, move1)
    print()
    print(b)
    if b.is_win_for(p.checker) == True:
        print(str(p) ,'wins in', str(p.num_moves), 'moves.')
        print('Congratulations!')
        return True
    elif b.is_full() == True:
        print("It's a tie!")
        return True
    else:
       return False
   
    
class RandomPlayer(Player):
      """can be used for an unintelligent computer player that chooses at 
      random from the available columns. This class should be a subclass 
      of the Player class"""
      def next_move(self, b):
          avail_col = []
          for i in range(b.width):
              if b.can_add_to(i) == True:
                  avail_col += [i]
          random_col = random.choice(avail_col)
          return random_col
      
         