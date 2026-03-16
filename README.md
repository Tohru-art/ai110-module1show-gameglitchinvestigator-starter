# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Purpose:** A number guessing game where the player picks a difficulty, then tries to guess a secret number within a limited number of attempts. Hints guide the player higher or lower after each guess.

**Bugs found:**
- Hints were backwards — "Go HIGHER!" showed when the guess was too high
- The secret was converted to a string on every even attempt, breaking the comparison
- Hard difficulty used range 1–50, which is smaller (easier) than Normal's 1–100
- The New Game button did not reset `status`, `score`, or `history`, leaving the game frozen after a win or loss

**Fixes applied:**
- Swapped the hint messages in `check_guess` in `logic_utils.py`
- Removed the string conversion — always compare using the integer secret
- Changed Hard range to 1–1000
- Reset all session state fields (`status`, `score`, `history`, `attempts`, `secret`) in the New Game block
- Refactored all game logic into `logic_utils.py` and added 16 pytest tests

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
