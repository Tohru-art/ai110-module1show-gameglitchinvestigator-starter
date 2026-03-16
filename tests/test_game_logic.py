from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score


# --- check_guess ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_high_hint_says_lower():
    # Hint message must tell the player to go lower when guess is too high
    _, message = check_guess(60, 50)
    assert "LOWER" in message

def test_too_low_hint_says_higher():
    # Hint message must tell the player to go higher when guess is too low
    _, message = check_guess(40, 50)
    assert "HIGHER" in message


# --- parse_guess ---

def test_parse_valid_integer():
    ok, value, _ = parse_guess("42")
    assert ok is True
    assert value == 42

def test_parse_empty_string():
    ok, value, _ = parse_guess("")
    assert ok is False
    assert value is None

def test_parse_none():
    ok, _, _ = parse_guess(None)
    assert ok is False

def test_parse_non_number():
    ok, _, err = parse_guess("abc")
    assert ok is False
    assert err == "That is not a number."

def test_parse_decimal_truncates():
    ok, value, _ = parse_guess("7.9")
    assert ok is True
    assert value == 7


# --- get_range_for_difficulty ---

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_hard_range_is_harder_than_normal():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high


# --- update_score ---

def test_win_adds_points():
    score = update_score(0, "Win", 1)
    assert score > 0

def test_too_low_subtracts_points():
    score = update_score(50, "Too Low", 1)
    assert score < 50

def test_score_never_goes_below_zero_on_win():
    # Even on a late attempt, score should gain at least 10
    score = update_score(0, "Win", 100)
    assert score >= 10
