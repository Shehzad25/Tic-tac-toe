🎮 Tic Tac Toe Game (Python – Human vs Computer)

A simple command-line Tic Tac Toe game built using Python where a human player competes against the computer. The user can choose their symbol (X or O), and the computer makes random valid moves.

📌 Features

Play Human vs Computer

Choose your symbol: X or O

Interactive CLI-based board

Input validation (no overwriting moves, valid positions only)

Automatic win detection

Random computer moves

🧠 Game Logic Overview

The board is represented using index positions (0–8):

0 | 1 | 2
--|---|--
3 | 4 | 5
--|---|--
6 | 7 | 8


Two lists track game state:

xstate → positions occupied by X

zstate → positions occupied by O

Winning combinations are checked after every move.

The computer selects a move randomly from available positions.

🛠️ Requirements

Python 3.x

No external libraries required (only built-in random module)

▶️ How to Run

Clone or download the repository

Navigate to the project directory

Run the script:

python main.py

🎯 How to Play

Choose your symbol (X or O)

Enter a number between 0 and 8 when prompted

The computer will automatically make its move

The game ends when either player wins

🧩 File Structure
.
├── main.py   # Main game logic
└── README.md # Project documentation

🏆 Win Conditions

A player wins if they occupy any one of the following:

Horizontal rows

Vertical columns

Diagonals

🚀 Possible Improvements (Future Scope)

Smarter AI using Minimax Algorithm

Draw detection

Replay option

GUI version (Tkinter / Pygame)

Multiplayer support

📄 Source Code

The complete implementation is available in main.py
