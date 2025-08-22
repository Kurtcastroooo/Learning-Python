# if = Do some code only IF some condition is True
#       Else do something



#Exercise 1
working_experience = float(input('How many years of experience do you have?: '))

if working_experience < 0:
    print('You have no working experience yet')
elif working_experience <= 2:
    print(f'You only have {working_experience} years of working experience and you not not qualified for this role')
elif working_experience == 3:
    print(f'You have {working_experience} years of working experience and may qualified for this role')
else:
    print(f'You have {working_experience} years of working experience and you are qualified for this role')



#Exercise 2
food = input('what food do you want to order: ') 
quantity = int(input('how many would you like?: ')) 

price = 10 if food == 'pandesal' else 20

total = price * quantity

if food:
    print(f'Yes we have {food} and it is price at {price} per piece')
    print(f'Your total is {total} Pesos')
elif food == '':
    print('You have not input and order')
else:
    print('No we do not have food')

#Exercise 3 Python Calculator

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ").strip()
num2 = float(input("Enter second number: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operator"

print(f"Result: {result}")

