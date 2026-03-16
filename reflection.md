# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
-------------------

1. The Hints are backwards; When your guess is too high, the game says go higher, and vice verca.

2. Secret number changes on even-numbered; every 2md attempt converts secret to a string, breaking the interger comparaison

3. Hard easier than normal; the range for hard is 1-50 which is easier and normal range was 1-100.


---

## 2. How did you use AI as a teammate?

I used Claude Code in VS Code to help find and fix bugs in this project.

**Correct suggestion:** Claude pointed out that the hints in `check_guess` were backwards — guessing too high showed "Go HIGHER!" when it should say "Go LOWER!". It also suggested moving the logic functions into `logic_utils.py` so they could be tested separately. I verified this by running `pytest` and confirming the hint tests passed.

**Incorrect/misleading suggestion:** The starter test file compared `check_guess()` directly to a string like `assert result == "Win"`. That was wrong because `check_guess` returns a tuple, not a plain string. I caught it by checking the function in `logic_utils.py` and rewrote the tests to unpack the tuple before asserting.

---

## 3. Debugging and testing your fixes

A bug was fixed when the matching pytest test passed and the game behaved correctly when I played it manually.

For the hints bug I ran `pytest tests/test_game_logic.py -v` and checked that `test_too_high_hint_says_lower` and `test_too_low_hint_says_higher` both passed. For the string conversion bug I opened the Developer Debug Info panel while playing and confirmed the secret stayed an integer on every attempt after the fix.

---

## 4. What did you learn about Streamlit and state?

Every time a user clicks a button or types anything, Streamlit reruns the entire script from top to bottom. That means any regular variable gets reset to its starting value on every interaction. `st.session_state` is how you keep values alive across those reruns — it acts like a small dictionary that persists between runs. The New Game bug was a good example of this: forgetting to reset `st.session_state.status` meant the game stayed frozen on "won" or "lost" even after clicking New Game, because the status check ran before the game could accept new input.

---

## 5. Looking ahead: your developer habits

One habit I want to keep is writing tests for logic functions before trusting that a fix works. Running pytest gave me confidence the hints and comparison bugs were actually fixed, not just appearing fixed in one manual test case.

Next time I work with AI on code I would read the AI's output more carefully before accepting it — the starter test file had a type mismatch that would have silently broken all three tests, and I only caught it by checking the function signature myself.

AI-generated code can look correct at a glance but still have subtle logic errors. This project showed me that AI is useful for spotting patterns and suggesting structure, but you still need to read and verify every change it makes.
