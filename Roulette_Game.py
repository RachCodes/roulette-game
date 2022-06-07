# Roulette Game

import random

black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
game_options = ["even/odd", "numbers", "under/over", "red/black"]
random_number = random.randint(0, 36)
print(random_number)

bet_choice = input("What would you like to bet on? [even/odd, numbers, under/over, red/black] ")
if bet_choice not in game_options:
    print("Error. Please replay and give a valid game type")
else:
    user_stake = float(input('How much do you want to bet? '))



# Choice 1: Numbers 0-36
if bet_choice == "numbers":

    user_number = float(input('Choose a number between 0 and 36 '))

    if user_number < 0 or user_number > 36:
        print('That is not a valid number you dum-dum')
    elif user_number % 1 != 0:
        print('Please select a whole number you massive dum-dum!')
    else:
        if user_number == random_number:
            print('You win! Your winnings are {}'.format(user_stake * 36))
        else:
            print('You lose. Better luck next time!')

# Choice 2: Even or odd
elif bet_choice == 'even/odd':
    user_evenodd = input("Even or odd? ")
    if user_evenodd != "even" and user_evenodd != "odd":
        print("Error. Please say 'even' or 'odd'")
    elif random_number == 0:
        print("You lose")
    elif user_evenodd == "even" and random_number % 2 == 0:
        print('You win! Woo! Your winnings are {}'.format(user_stake * 2))
    elif user_evenodd == "odd" and random_number % 2 != 0:
        print('Woo, you win! Happy days! Your winnings are {}'.format(user_stake * 2))
    else:
        print('You lose. Haha.')

# Choice 3: Under/Over
elif bet_choice == 'under/over':
    user_underover = input("Under or over? ")
    if user_underover != "under" and user_underover != "over":
        print("Error. Please say 'under' or 'over'")
    elif random_number == 0:
        print("You lose")
    elif user_underover == "under" and random_number <= 18:
        print('You win! Woo! Your winnings are {}'.format(user_stake * 2))
    elif user_underover == "over" and random_number >= 19:
        print('Woo, you win! Happy days! Your winnings are {}'.format(user_stake * 2))
    else:
        print('You lose. Haha.')

# Choice 4: Red or black
elif bet_choice == "red/black":
    user_redorblack = input("Red or black? ")
    if user_redorblack != "red" and user_redorblack != "black":
        print("Error. Please say 'red' or 'black'")
    elif random_number == 0:
        print("You lose")
    elif user_redorblack == "black" and random_number in black_numbers:
        print("You win! You win {}".format(user_stake * 2))
    elif user_redorblack == "red" and random_number in red_numbers:
        print("You win {}! Yay!".format(user_stake * 2))
    else:
        print("You lose")