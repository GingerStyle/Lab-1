#creating list to hold classes the user is taking
classes = list()
#getting the classes the user is taking
more = True
while more == True:
    user_class = input('Enter a class you are taking. ')
    #adding class to list
    classes.append(user_class)
    #asking if there are more classes to add
    more_question = input('Are there other classes you are taking? ')
    if more_question.upper() != 'YES':
        more = False
#displaying the list
for string in classes:
    print(string)