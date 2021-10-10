from random import randint


# generate random number between 1 and level of difficulty
def generate_number(num1):
    return randint(1, num1)


# get guess from user according to level of difficulty
def get_guess_from_user(num2):
    # show the user the range of numbers
    def select(select_question, min_num, max_num):
        while True:
            try:
                # get number from user and assigned it to var
                # if it cannot convert to int it falls to value error exception
                chosen_num = int(input(select_question + ' ' + str(min_num) + '-' + str(max_num) + ': '))
                # return the chosen number and quit
                return chosen_num
                break
            # user enter value that is not int
            except ValueError:
                continue

    # execute the question
    return select('Guess a number between', 1, num2)


# compare results and return True or False according to comparison
def compare_results(user, computer):
    return user == computer


# execute the game according to level of difficulty
def play(difficulty):
    # cast number between 1 and level of difficulty
    secret_number = generate_number(difficulty)
    # get guess from user and show him the range of numbers
    guess_from_user = get_guess_from_user(difficulty)
    # run comparison between user and computer
    result = compare_results(guess_from_user, secret_number)
    # print('guess from user', guess_from_user)
    # print('secret number', secret_number)
    # print(result)
    # return True or False
    return result
