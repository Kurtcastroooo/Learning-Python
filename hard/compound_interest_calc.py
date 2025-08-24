# Python compound interest calculator

principal = 0
rate = 0
time = 0

# while principal <= 0:
#     principal = float(input("Enter the principal amount: "))
#     if principal <= 0:
#         print("Principal must be greater than 0.")

# while rate <= 0:
#     rate = float(input("Enter the annual interest rate: "))
#     if rate <= 0:
#         print("Rate must be greater than 0.")

# while time <= 0:
#     time = int(input("Enter the time in years: "))
#     if time <= 0:
#         print("Time must be greater than 0.")

# # print(principal, rate, time)

# total = principal * (1 + rate / 100) ** time

# print(f"balance after {time} years: ${total:.2f}")

while True:
    principal = float(input("Enter the principal amount: "))
    if principal <0:
        print("Principal must be greater than 0.")
    else:
        break

while True:
    rate = float(input("Enter the annual interest rate: "))
    if rate <0:
        print("Rate must be greater than 0.")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time <0:
        print("Time must be greater than 0.")
    else:
        break 

total = principal * (1 + rate / 100) ** time

print(f"balance after {time} years: ${total:.2f}")
