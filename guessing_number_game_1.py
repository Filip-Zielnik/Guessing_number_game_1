from random import randint


def guess_the_number():
    """
    Game asks user to guess the random number from 1 to 100.
    :return: Too small!, Too big! or You win!
    """
    computer_choice = randint(1, 100)  # computer draws a random number from 1 to 100
    while True:
        try:
            user_guess = int(input("Guess the number: "))  # user selects the number
            if user_guess > computer_choice:
                print("Too big!")
            elif user_guess < computer_choice:
                print("Too small!")
            else:
                print("You win!")
                break
        except ValueError:
            print("It's not a number!")


guess_the_number()
