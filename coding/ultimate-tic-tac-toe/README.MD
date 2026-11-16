# Ultimate Tic Tac Toe

Nine games of tic-tac-toe inside one big one. The cell you pick in a small board decides which board your opponent has to play in next. Win a small board to claim it; win three small boards in a row to win the game.

## How to play

```
python3 ultimate_tic_tac_toe.py
```

Boards and cells are both numbered 0–8, left to right and top to bottom:

```
0|1|2
-+-+-
3|4|5
-+-+-
6|7|8
```

Player 1 (X) starts on any board. After that, each move sends the other player to the board matching the cell just played. If that board has already been won, they can pick any open board.

Written by Alexander in Python.
