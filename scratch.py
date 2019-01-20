#getting user input
name = input('What is your name? ')
birth_month = input('What is your birth month? ')
#printing messages
print('Hello there ' + name)
if birth_month.upper() == "JANUARY":
    print('Happy Birthday this month')
print('There are ' + str(len(name)) + ' letters in your name')
