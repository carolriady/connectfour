#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from board import *
from player import Player

class AIPlayer(Player):
    """“AI player” will look ahead some number of moves into the future to 
    assess the impact of each possible move that it could make for its 
    next move, and it will assign a score to each possible move. it will 
    then choose as its next move the column with the maximum score. 
    This will be the player’s judgment of its best possible move."""
    
    def __init__(self, checker, tiebreak, lookahead):
        """constructs a new AIPlayer object"""
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):
        """returns a string representing an AIPlayer object."""
        return 'Player ' + str(self.checker) + ' (' + str(self.tiebreak) + ', ' + str(self.lookahead) + ')'
    
    def max_score_column(self, scores):
        """takes a list scores containing a score for each column of the board, 
        and that returns the index of the column with the maximum score."""
        max_score = max(scores)
        list_indices = []
        result = 0
        for i in range(len(scores)):
            if scores[i] == max_score:
                list_indices += [i]
        if len(list_indices) > 1:
            if self.tiebreak == 'LEFT':
                result = list_indices[0]
            elif self.tiebreak == 'RIGHT':
                result = list_indices[-1]
            else:
                result = random.choice(list_indices)
        else:
            result = list_indices
        return result
    
    def scores_for(self, b):
        """takes a Board object b and determines the called AIPlayer‘s 
        scores for the columns in b. The method should return a list containing 
        one score for each column."""
        scores = [50] * b.width
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opponent =  AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opponent.scores_for(b)
                scores[col] = 100 - max(opp_scores)   
               
                
               #if max(opp_scores) == 100:
                    #scores[col] = 0
                #elif max(opp_scores) == 50:
                    #scores[col] = 50
               # elif max(opp_scores) == 0:
                    #cores[col] = 100
                b.remove_checker(col)
                
        return scores
    
        
    def next_move(self, b):
        """overrides (i.e., replaces) the next_move method that is inherited 
        from Player. Rather than asking the user for the next move, 
        this version of next_move should return the called AIPlayer‘s 
        judgment of its best possible move."""
    
        self.num_moves += 1
        
        scores = self.scores_for(b)
        return self.max_score_column(scores)
        
        
        
        