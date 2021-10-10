from currency_converter import CurrencyConverter
from random import randint

# check online and convert 1$ to ₪. round the number to 2 digit after decimal point
# save the value to t
t = round(CurrencyConverter().convert(1, 'USD', 'ILS'), 2)


# create interval tuple - range according to level of difficulty
def get_money_interval(d):
    interval = (t - (5 - d), t + (5 - d))
    return interval


# get guess from user
def get_guess_from_user():
    # cast amount of money between 1$ to 100$ (both endpoints included in this lib)
    rand_num = randint(1, 100)
    while True:
        try:
            # get number from user and show him the amount of dollar he need to guess in ILS
            # if he enter value that cannot convert to float it falls to exception
            chosen_num = float(input(f'Please enter the amount of ₪ of {str(rand_num)}$: '))
            # return tuple contain the user guess and the random dollar amount
            return chosen_num, rand_num
        # user enter value that is not float
        except ValueError:
            # repeat
            continue


# execute the game
def play(difficulty):
    # run get money interval according to level of difficulty
    # return tuple range according to 1 dollar
    interval = get_money_interval(difficulty)
    # print(t)
    # print(interval[0])
    # print(interval[1])
    # save the guess from user and the casting dollar amount to tuple
    question = get_guess_from_user()
    # extract the user guess from question and save it to user_choice
    user_choice = question[0]
    # extract the casting amount of dollar and save it cast_usd
    cast_usd = question[1]
    # take the low amount from interval tuple, multiply it by cast usd amount
    # round the whole number to 2 digits after decimal point
    # save it to variable
    low_multiple_random_dollar = round((interval[0] * cast_usd), 2)
    # exactly as in the previous variable - but to high amount
    high_multiple_random_dollar = round((interval[1] * cast_usd), 2)
    # print(low_multiple_random_dollar)
    # print(high_multiple_random_dollar)
    # print(user_choice)
    # return comparison if the user amount guess is between the range of the selected interval (according to difficulty)
    return low_multiple_random_dollar <= user_choice <= high_multiple_random_dollar

# print(play(3))
# print(get_money_interval(3))
# print(get_guess_from_user())
