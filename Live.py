import GuessGame
import MemoryGame
import CurrencyRouletteGame
import time
import Utils
import Score


def welcome(name):
    return f'Hello {name} and welcome to the World of Games (WoG).\n' \
           f'Here you can find many cool games to play.'


def load_game():
    """
    This function will load the games
    """
    print('Please choose a game to play:\n'
          '\t1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n'
          '\t2. Guess Game - guess a number and see if you chose like the computer.\n'
          '\t3. Currency Roulette - try and guess the value of a random amount of USD in ILS')

    # func that print question, let user select between 2 int
    def select(select_quest, min_num, max_num):
        while True:
            try:
                # get number from user and assigned it to var
                # if it cannot convert to int it falls to value error exception
                chosen_num = int(input(select_quest + ' ' + str(min_num) + '-' + str(max_num) + ': '))
                # check if the entered value between 2 int, if yes return the value and go out
                if min_num <= chosen_num <= max_num:
                    return chosen_num
                    break
                # if not repeat the loop
                else:
                    continue
            # user enter value that is not int
            except ValueError:
                continue

    # execute game selection and save it to game
    game = select('Please select game', 1, 3)
    # execute difficulty selection and save it to difficulty
    difficulty = select('Please choose game difficulty from', 1, 5)
    # if user select MemoryGame
    if game == 1:
        # execute game and save the boolean if won True if lost False
        won_or_not_game_1 = MemoryGame.play(difficulty)
        # if won declare it and let user play another game
        if won_or_not_game_1:
            print('You won Memory Game!!!')
            time.sleep(1)
            Utils.screen_cleaner()
            Score.add_score(difficulty)
            load_game()
        # if lost print game over and quit
        else:
            print('Game Over!!')
            time.sleep(1)
            Utils.screen_cleaner()
    # if user select GuessGame
    if game == 2:
        # execute game and save the boolean if won True if lost False
        won_or_not_game_2 = GuessGame.play(difficulty)
        # if won declare it and let user play another game
        if won_or_not_game_2:
            print('You Won Guess Game!!!')
            time.sleep(1)
            Utils.screen_cleaner()
            Score.add_score(difficulty)
            load_game()
        # if lost print game over and quit
        else:
            print('Game Over!!')
            time.sleep(1)
            Utils.screen_cleaner()
    if game == 3:
        won_or_not_game_3 = CurrencyRouletteGame.play(difficulty)
        if won_or_not_game_3:
            print('You Won Currency Roulette Game!!!')
            time.sleep(1)
            Utils.screen_cleaner()
            Score.add_score(difficulty)
            load_game()
        else:
            print('Game Over!!')
            time.sleep(1)
            Utils.screen_cleaner()
