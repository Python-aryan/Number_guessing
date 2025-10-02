
# Number Guessing Game 🕹️

A simple and fun Python-based number guessing game. The system picks a random number in a user‑specified range, and the player must guess it in as few attempts as possible.

---

## 📋 Table of Contents

* [About](#about)
* [Features](#features)
* [How It Works](#how-it-works)
* [Getting Started](#getting-started)

  * [Prerequisites](#prerequisites)
  * [Installation & Running](#installation--running)
* [Usage Example](#usage-example)
* [Possible Improvements / Extensions](#possible-improvements--extensions)
* [Contributing](#contributing)
* [License](#license)

---

## ℹ️ About

**Number_guessing** is a command-line game where the user defines a numeric range (e.g. 1 to 100), and the program randomly selects a number within that range. The user then guesses repeatedly, and after each guess is told whether their guess is too high, too low, or correct—until they find the number.

This is a good beginner project to practice:

* Input / output
* Control flow (loops, conditionals)
* Error handling
* Random number generation
* Simple game logic

---

## ✅ Features

* User specifies the lower and upper bounds of the range
* Random number is generated in that range
* After each guess, feedback is given: “Too high”, “Too low”, or “Correct”
* Keeps track of number of attempts
* Validates user input (e.g. non‑numbers, guesses outside range)
* (Optional) A little ASCII art / fun touches if you include in `art.py`

---

## ⚙️ How It Works

1. Ask the user for the lower bound `A` and upper bound `B`
2. Generate a random number `target` in `[A, B]`
3. Loop until user guesses `target`:

   * Prompt user for a guess
   * If guess < target → print “Too low”
   * If guess > target → print “Too high”
   * Else → print “Congratulations! You guessed it in N tries.”
4. Optionally, offer to play again

This game essentially practices **binary‑search style narrowing** of the range by feedback, though user does the logic manually.

---

## 🛠 Getting Started

### Prerequisites

* Python 3.x
* Basic knowledge of running Python scripts from terminal / command line

### Installation & Running

1. Clone the repo:

   ```bash
   git clone https://github.com/Python-aryan/Number_guessing.git
   cd Number_guessing
   ```

2. Optionally, use a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # on macOS / Linux
   # or `.\venv\Scripts\activate` on Windows
   ```

3. Run the game:

   ```bash
   python guessing.py
   ```

   (If there are other entry‑point scripts, you may also run `art.py` or combined driver script.)

---

## 🎮 Usage Example

```
Welcome to Number Guessing Game!
Enter the lower bound: 1
Enter the upper bound: 100

I have picked a number between 1 and 100. Try to guess it!

Your guess: 50  
Too high.

Your guess: 25  
Too low.

Your guess: 37  
Too low.

Your guess: 45  
Too high.

Your guess: 40  
Correct! You guessed it in 5 tries.  
```

If the user inputs invalid data (non-integer, out of range, etc.), your program should catch that and prompt again.

---

## 🚀 Possible Improvements / Extensions

Here are ideas you (or others) can build on:

* **Replay / Loop** — After finishing, ask user if they want to play again.
* **Difficulty Levels** — Fixed ranges (easy, medium, hard) with different limits.
* **Hints** — Offer hints (“You’re within 10”, “Warm / Cold”)
* **Leaderboard / High Score** — Save the minimum attempts across sessions.
* **Graphical UI / Web UI** — Use Tkinter, PyQt, or a web interface.
* **Multiplayer mode** — Two players alternate, or guesser vs setter.
* **Timing / Score** — Add a timer or scoring based on speed + guesses.
* **Logging / History** — Store past games, statistics.

---

## 🤝 Contributing

Contributions are welcome! You can help by:

1. Forking the repo
2. Creating a branch for your feature (e.g. `feature/hints`)
3. Making your changes / adding tests / updating README
4. Submitting a pull request

Be sure to describe what you changed or added, and test that everything works.

---

## 📄 License

Add your project license here (e.g. MIT, Apache‑2.0). If you don’t have one yet, you may use:

```
MIT License

Copyright (c) 2025 <Your Name>

Permission is hereby granted, free of charge, to any person obtaining a copy
… (rest of MIT text) …
```

