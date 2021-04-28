import random


def color(key):
    return "\033[33mblack \033[0m" if key == 1 else "white "


def view_question(key):
    first_question = "Would you like to start play? "
    other_question = "Would you like to play again?"
    return True if input(first_question if key == 0 else other_question) in "YyДд" else False


def throw():
    while True:
        player_number = input("Input a number from 1 to 10")
        if player_number and player_number.isdigit() and 10 >= int(player_number) >= 1:
            return int(player_number)
        print("Bad choise!")


def winner():
    return "WINNER!" if game_info["Player"] > game_info["Ai"] else \
        ("LOOSER!" if game_info["Player"] < game_info["Ai"] else "DRAWing!")


def action():
    r = random.randint(1, 3)
    a = random.randint(1, 20)
    b = random.randint(20, 40)
    if r == 1:
        print("Good" if int(input(f"{a}+{b} = ")) == a + b else "Bad")
    elif r == 2:
        print("Good" if int(input(f"{b}-{a} = ")) == b - a else "Bad")
    else:
        print("Good" if int(input(f"{b}%{a} = ")) == b % a else "Bad")


if __name__ == '__main__':
    # TASK 1
    """
    The Guessing Game.

    Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. 
    The result should be sent back to the user via a print statement.
    """

    print(" Task 1 ", sep='*')
    game_info = {"Player": 0, "Ai": 0, "Count_round": 0, "key": 0}
    while view_question(game_info['key']):
        game_info['key'] = 1
        if throw() > random.randint(1, 10):
            game_info["Player"] += 1
            print("You WIN! ")
            continue
        else:
            game_info["Ai"] += 1
            print("You LOSE! ")
            continue
        print("It's DRAW! ")

    print(f"Thank for game! Your are\033[31m {winner()}\033[0m\nScore: \033[32m \nPlayer "
          f"{game_info['Player']}\033[0m:\033[33m{game_info['Ai']} AI\033[0m")

    # TASK 2
    """
    The birthday greeting program.

    Write a program that takes your name as input, and then your age as input and greets you with the following:
    
    “Hello <name>, on your next birthday you’ll be <age+1> years”   
    """

    print(" Task 2 ", sep='*')
    name = input('Write your name ')
    while True:
        years = input('How old are you?')
        if not years.isdigit():
            continue
        break
    print(f"Hello {name}, on your next birthday you’ll be {int(years)+1} years")

    # TASK 3
    """
    Words combination
    
    Create a program that reads an input string and then creates and prints 5 random strings 
    from characters of the input string.
    
    For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) 
    that combine characters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …
    
    Tips: Use random module to get random char from string)
    """

    print(" Task 3 ", sep='*')
    some_word = input("Write word - ")
    li = []
    li[:0] = some_word
    i = 0
    while i < 5:
        random.shuffle(li)
        print(li)
        i += 1

    # TASK 4
    """
    The math quiz program

    Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, 
    and then responds with a message accordingly.
    """

    print(" Task 4 ", sep='*')
    i = 0
    while i < 3:
        action()
        i += 1

    # TASK *
    print("Task * ", sep='*')
    i = 0
    j = 0
    # key: (1 - black; -1 - white)
    key = 1
    while i < 8:
        i += 1
        if j == 8:
            j = 0
            print()
            key *= -1
        while j < 8:
            j += 1
            print(color(key), end='')
            key *= -1
