from classes import *

def test_is_answer_correct_true():
    game = Mastermind()
    assert game.is_answer_correct(game.color_number * "+") is "correct"


def test_is_answer_correct_false():
    game = Mastermind()
    assert game.is_answer_correct(game.color_number * "-") is "incorrect"
    assert game.is_answer_correct("+++++-") is "incorrect"
    assert game.is_answer_correct("-+++++") is "incorrect"
    assert game.is_answer_correct(game.color_number * "++") is "incorrect"


def test_new_game():
    game = Mastermind()
    assert game.new_game(["R", "G", "B", "O", "W", "P", "L", "S", "K", "V"]) is game.color_code
    assert game.new_game(["A", "D", "C", "E", "F", "H", "I", "J", "M", "N"]) is game.color_code


def test_new_game_too_less_codes():
    game = Mastermind()
    try:
        game.new_game(["R", "G", "B"]) 
    except ValueError as e:
        assert isinstance(e, ValueError)


def test_is_guess_valid_true():
    game = Mastermind()
    game.color_code = ["R", "O", "P", "G"]
    assert game.is_guess_valid("ROPG") is True


def test_is_guess_valid_false():
    game = Mastermind()
    game.color_code = ["R", "G", "B", "W"]
    assert game.is_guess_valid("ABCD") is False 
    assert game.is_guess_valid("WXYZ") is False 


def test_next_round_true():
    game = Mastermind()
    for i in range(game.max_retries - 1):
        assert game.next_round() is False
        
    assert game.next_round() is True


def test_congratulate_true():
    game = Mastermind()
    print("case1=", game.trys != 0)
    print("case2=", game.trys)
    assert game.congratulate(0) is True


def test_congratulate_false():
    game = Mastermind()
    assert game.congratulate(1) is False
    assert game.congratulate(2) is False
    assert game.congratulate(3) is False
    assert game.congratulate(12) is False


def test_retry_or_exit_true():
    game = Mastermind()
    assert game.retry_or_exit("J") is True


def test_retry_or_exit_false():
    game = Mastermind()
    assert game.retry_or_exit("N") is False

