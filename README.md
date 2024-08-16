# Hangman Game

## Overview

This is a beginner-level Python implementation of the classic "Hangman" game. The game randomly selects a movie name from a predefined list, and the player has to guess the letters in the movie name within a limited number of attempts.

## Project Structure

The project consists of three Python files:

1. **db.py**: Contains a list of movie names that the game can choose from.
2. **module.py**: Contains the functions used in the game, such as displaying the hangman and the partially guessed movie name.
3. **main.py**: This is the main file that runs the game logic.

## How to Play

1. **Run the `main.py`**: The game will start by randomly selecting a movie name.
2. **Guess the Letters**: Enter letters one by one to guess the movie name.
3. **Winning**: If you guess all the letters correctly before running out of attempts, you win!
4. **Losing**: If you exceed the maximum number of wrong attempts, you lose the game.

## Usage

To play the game, simply run the `main.py` file:

```bash
python main.py

```

## Example Output:

```bash
Movie Hint: - a - - a -
Enter Character: b
Your Guess was Correct!!
b is there in the movie name

Number of Wrong Answers: 0
Correct Alphabets guessed: ['b']

```

## Future Improvements

* Add more movie names to the list.
* Implement a graphical user interface (GUI).
* Allow for multiple rounds in a single game session.
