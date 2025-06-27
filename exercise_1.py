# Exercise 1 -- Rectange Area Calc

length = float(input('what is the length of the rectangle?:'))
width = float(input('what is the width of the rectangle?:'))

area = length * width

print(f'The area of the rectangle is {area} cm2.')

# Exercise 2 -- Shopping Cart Program

item = input('what would you like to buy?:')
price = float(input('what is the price?:'))
quantity = int(input('how many would you like?'))

total = price * quantity

print(f'You have bought {quantity} x {item}/s')
print(f'your total is: ${total}')