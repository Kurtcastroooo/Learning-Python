# Logical Operators = evaluate multiple conditions (or, and, not)
#                    or = at least one condition must be True
#                    and = both conditions must be True
#                    not = inverts the condition (not False, not True)

temp = int(input('Enter the temperature: '))
is_sunny = True
is_raining = True


if is_sunny and temp > 37:
    print('It is hot outside 🔥')
elif is_raining and not is_sunny:
    print('It is raining in Manila 🌧')
elif is_raining or is_sunny and temp <=37:
    print('Not sure of the weather but we have a chill temperature')
else:
    print('I am not sure of the current weather and temp')