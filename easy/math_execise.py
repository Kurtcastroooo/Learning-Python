#Exercise 1

import math as mt

radius = float(input('Enter radius of a circle '))

circumference = mt.pi * radius

print(f'the circumference is: {round(circumference)} cm')

#Exercise 2

radius = float(input('Enter radius of a circle '))

area =  mt.pi * pow(radius,2)

print(f'the area of the circle is: {round(area,2)} cm')

#Exercise 3

a = float(input('Enter the length of side a '))
b = float(input('Enter the length of side b '))

c = mt.sqrt(pow(a,2) + pow(b,2))

print(f'the length of side c is: {round(c,2)} cm')