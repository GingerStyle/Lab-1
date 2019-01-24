# welcome message
print('Welcome User')
#get user sentence
sentence = input('Enter a sentence to convert to camel case. Include spaces, no punctuation')
#chop up sentence into words
word_list = sentence.split(' ')
#capitalize words except for first word
camelCase_list = (word_list[0] if word_list.index(x) == 0 else x.capitalize() for x in word_list)
#print out result
for string in camelCase_list:
    print(string, end='')
