# String methods examples

# name = input('Enter your name: ')

# result = len(name.replace(' ',''))

# print(f'Your name is {name} and it has {result} characters')

name ='Kato Riamu'

phone_number = '134-134-22-1-4'

result = name.find(' ')

result = name.rfind('R')

result = name.capitalize()

result = name.upper()

result = name.lower()

result = name.isdigit()

result = name.isalpha()

result = phone_number.count('-')

result = phone_number.replace('-',' ')
 

print(result)

print(help(str))

# Exercise 
# username cannot contain more than 12 characters
# username cannot contain spaces
# sername cannot contain Numbers and special characters

username = input('Enter your username')

if len(username) > 12:
    print('your username cannot contain more than 12 characters')
elif not username.find(' ') == -1:
    print('your username cannot contain spaces')
elif not username.isalpha():
    print('your username cannot contain Numbers and special characters')
else:
    print(f'welcome to my vlog {username}') 