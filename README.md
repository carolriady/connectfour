# connectfour

Connect Four is a variation of tic-tac-toe played on a 6x7 rectangular board.

The game is played by two players, and the goal is to place four checkers in a row vertically, horizontally, or diagonally. The players alternate turns and add one checker to the board at a time. However, because the board stands vertically, a checker cannot be placed in an arbitrary position on the board. Rather, a checker must be inserted at the top of one of the columns, and it “drops down” as far as it can go – until it rests on top of the existing checkers in that column, or (if it is the first checker in that column) until it reaches the bottom row of the column.

The standard board size for Connect Four is six rows of seven columns, but your Board class should be able to handle boards of any dimensions. However, for simplicity we will preserve the four-in-a-row requirement for winning the game regardless of the board size (even for boards with dimensions less than 4x4).

In this cod4e, I define a more “intelligent” computer player – one that uses techniques from artificial intelligence (AI) to choose its next move.

In particular, this “AI player” will look ahead some number of moves into the future to assess the impact of each possible move that it could make for its next move, and it will assign a score to each possible move. And since each move corresponds to a column number, it will effectively assign a score to each column.




