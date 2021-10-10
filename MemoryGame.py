from random import randint
import time


# generate list of numbers according to level of difficulty
def generate_sequence(length1):
    # create empty list
    computer_list = []
    # run the loop number of times according to level of difficulty
    for _ in range(0, length1):
        # add random number to list in range 1-101 (end points are included)
        computer_list.append(randint(1, 101))
    # return the full list
    return computer_list


# get from user list of numbers according to level of difficulty
def get_list_from_user(length2):
    # create empty list
    user_list = []
    # run the loop number of times according to level of difficulty
    # each time the user enter the memorized number
    for _ in range(0, length2):
        while True:
            try:
                # use this dictionary in the message and convert numbers to words
                number_to_word = {0: "first", 1: "second", 2: "third", 3: "forth", 4: "fifth"}
                # return cursor to the start
                print('\r', end='')
                # let user enter number
                chosen = input(f'Please guess the {number_to_word[_]} number: ')
                # if user enter value that is not number it fail to exception
                # if not, the string entered converted to int
                chosen = int(chosen)
                # the number is added to user_list and quit
                user_list.append(chosen)
                break
            except ValueError:
                # fall to exception, repeat.
                continue

    # return the user_list filled by the user
    return user_list
    # print(user_list)


# check if user list is equal to computer list and return True or False
def is_list_equal(user, computer):
    return user == computer


# execute the game according to level of difficulty
def play(difficulty):
    # computer generate list of random numbers
    computer_sequence = generate_sequence(difficulty)
    # this message will show to the user
    msg = "Please memorize the above numbers!!"
    # set the delay time between prompts
    delay = 2
    # print the above msg and not enter new line
    print(msg, end='')
    # delay
    time.sleep(delay)
    # erase the msg from screen
    print('\r' + ' ' * len(msg), end='')
    # return the cursor to start
    print('\r', end='')
    # delay
    time.sleep(delay)
    # show the user the computer numbers one by one
    for num in computer_sequence:
        # convert the number to str according to print it as string
        num = str(num)
        # return the cursor to start
        print('\r', end='')
        # print the number without enter new line
        print(num, end='')
        # delay so user can memorize
        time.sleep(delay)
        # return cursor to start end erase the number
        print('\r' + ' ' * len(num), end='')
    # execute get list of numbers from user
    list_from_user = get_list_from_user(difficulty)
    # print(computer_sequence)
    # print(list_from_user)
    # return comparison between user list and computer list as boolean
    return list_from_user == computer_sequence

# print(play(3))
# get_list_from_user(3)
# print(66)
