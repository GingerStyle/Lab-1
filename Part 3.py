from random import randint
#generate random number for user to guess
computer_number = randint(1,10)
#asking user for input
user_guess = input('Guess a number between 1 and 10. ')
#processing answer
while int(user_guess) != computer_number:
    if int(user_guess) > computer_number:
        print('Your guess is too high.')
        user_guess = input('Guess another number. ')
    elif int(user_guess) < computer_number:
        print('Your guess is too low.')
        user_guess = input('Guess another number. ')
#when guess is correct, tell the user
print('You are right! The number was ' + str(computer_number) + '!')
