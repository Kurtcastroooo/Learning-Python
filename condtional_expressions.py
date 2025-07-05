# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          print or assign one of two values based on a condition
#                          x if condition else y

num = 5
a = 6
b = 7
user_role = 'guest'
person = 'MotherFucker!'

result = 'Positive' if num > 0 else 'Negative'

result = 'Even' if a % 2 == 0 else 'Odd'

result = 'Full Access' if user_role == 'Admin' else f'Limit Access to {person}'

print(result)