# While loop = executes some code WHILE some condition remains true.

name = input("Enter your name: ")
age =  input("Enter your age: ")
food = input("Enter your favorite food: ")

age = int(age)

while name == "":
    print("You didn't enter your name!")
    name = input("Enter your name: ")
print(f"Hello {name}")

while age < 0 or age > 120:
    if age > 120:
        print("You can't be more than 120 years old!")
    elif age < 0:
        print("You can't be less than 0 years old!")
    age = int(input("Enter your age: "))
print(f"You are {age} years old")

while not food == "q":
    print(f"Your favorite food is {food}")
    food = input("Enter your favorite food (or 'q' to quit): ")
print("Bye!")