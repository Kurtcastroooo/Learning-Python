# for loops = execute a block of code a fixed number of times.
#             you can iterate over a sequence (string, list, tuple, set, dictionary)
#             range (start, stop, step)
#             continue = skip to the next iteration of the loop
#             break = exit the loop

# for x in range(1,11):
#     print(x)
# print("Done")

# for x in reversed(range(1,11)):
#     print(x)
# print("Happy New Year!")

# credit_card_number = "1234-5678-9012-3456"

# for x in credit_card_number: 
#     print(x)

for x in range(1,21):
    if x == 13:
        continue
    else:
        print(x)