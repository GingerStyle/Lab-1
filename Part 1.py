#getting user input
name = input('What is your name? ')
birth_month = input('What is your birth month? ')
#printing messages
print('Hello there ' + name)
#deciding if your birthday is in January
if birth_month.upper() == "JANUARY":
    print('Happy Birthday this month')
#printing number of letters in the user's name
print('There are ' + str(len(name)) + ' letters in your name')
