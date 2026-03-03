import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# continue here

# loop through each index so we can modify the list in place
for i in range(len(random_numbers)):
    n = random_numbers[i]
    if n > 80:
        # replace numbers greater than 80 with their negative value
        random_numbers[i] = -n
    elif n < 40:
        # replace numbers lower than 40 with the sum of their digits
        # e.g. 39 -> 3//10=3, 39%10=9, 3+9=12
        random_numbers[i] = n // 10 + n % 10

print(random_numbers)
