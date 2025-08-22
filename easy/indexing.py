# Indexing = accessing elements of a sequence using [] (Indexing Operator)
#           [Start : end : step]

credit_card_number = '1234 5678 9012 3456'

print(f"First Character = {credit_card_number[0]}")  # First character

print(f"First up to 4th Char {credit_card_number[0:4]}") # First 4 characters

print(f"From 5 up to all the last Characters = {credit_card_number[5:]}")

print(f"Last 4 Characters = {credit_card_number[-4:]}")

print(f"Every other Character = {credit_card_number[::2]}")  # Every other character

last_digits = credit_card_number[-4:]

print(f"Last 4 Digits = {last_digits}")

reversed_cc = credit_card_number[::-1]
print(f"Reversed CC Number = {reversed_cc}")