# Number Guessing Game

A simple terminal game where you set a range and try to guess the secret number in as few attempts as possible.

### Features
- **Custom range**: choose any integer lower and upper bounds.
- **Smart attempt limit**: you get about log2(range) attempts (rounded up).
- **Input validation**: friendly prompts for invalid or out‑of‑range inputs.
- **Fun ASCII banners**: randomized game logo from `art.py`.

## Requirements
- Python 3.7+

## Run
From the `Number_guessing` directory:

```bash
python guessing.py
```

## How to Play
1. Enter a lower and upper bound (integers). If you enter the same number for both, the range contains a single value.
2. The game picks a secret number within your range.
3. You have a limited number of attempts to guess it. After each guess you’ll see whether it’s too high or too small, plus how many attempts remain.
4. Guess correctly within the limit to win; otherwise the game reveals the number.

### Attempt Limit
The number of chances is calculated as: ceil(log2(upper − lower + 1)). This mirrors an optimal binary‑search strategy.

## Example Session
```text
████ Game banner (randomized) ████
Welcome to the Number Guessing Game!
Enter Lower bound:- 1
Enter Upper bound:- 100

    You've only 7 chances to guess the integer number!

Guess a number: 50
You guessed too high!
Attempts remaining: 6

Guess a number: 25
You guessed too small!
Attempts remaining: 5

... (more guesses) ...

Congratulations you guessed it in 4 tries
```

## Tips
- Start by guessing near the middle of the current range to narrow it quickly.
- Pay attention to the remaining attempts displayed after each guess.

## Files
- `guessing.py`: main game logic.
- `art.py`: list of ASCII art banners used at startup.

## Contributing
Pull requests to improve the game (UX, features, or code quality) are welcome. Please keep the game simple and beginner‑friendly.

## License
MIT
