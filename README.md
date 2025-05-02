# Guess-The-Number# Number Guessing Game with Timer

This is a Python-based number guessing game where the player has 5 seconds to guess a randomly chosen number between 1 and 10. The game will automatically terminate if the player doesn't provide a valid input within the given time frame.

## Features
- **Random Number Generation**: The game generates a random number between 1 and 10 for each round.
- **5-Second Timer**: Each guess must be made within 5 seconds, or the attempt will automatically fail.
- **Exit Option**: The player can type `exit` to quit the game at any time.
- **Multiple Rounds**: The game runs for 3 attempts per round before ending.

## Requirements

- Python 3.x
- `threading` module (This comes pre-installed with Python)

## How to Run the Game

1. Make sure Python 3.x is installed on your system.
2. Download the `guessing_game.py` file (or save the code provided above).
3. Open a terminal (Command Prompt, PowerShell, or terminal emulator) and navigate to the directory containing the file.
4. Run the game using the following command:
   ```bash
   python guessing_game.py
## Game Rules
A random number between 1 and 10 is selected by the system.

The player has 5 seconds to guess the number.

If the player guesses the correct number, a success message is displayed.

If the player doesn't guess correctly, the system will notify the player and give them another chance.

The player can type exit at any time to quit the game.

The game allows a total of 3 attempts for each round.

## sample output
New game starting...
3
2
1
(Press 'exit' to quit)

Guess the number (1-10): 5
Time's up!
You guessed the wrong answer. Try again!

Guess the number (1-10): 7
Time's up!
You guessed the wrong answer. Try again!

Guess the number (1-10): 8
You guessed the wrong answer. Try again!

Sorry, you used all attempts. The number was 3.



