# Variables
# A container for a value (string, integer, float , boolean)
# behaves as if it was the value it contains.

#String
first_name = 'Kato'

last_name = 'Riamu'

full_name = f'My Full name is {first_name} {last_name}'

#Integer
age = 21

#Float
height = 5.2

#Bool
working = True 


#Sample Logic

if height <= 5.2 and working:
    print(full_name)
elif age == 25 and not working:
     print('Tambay')
else:
     print('Youre missing a statement')