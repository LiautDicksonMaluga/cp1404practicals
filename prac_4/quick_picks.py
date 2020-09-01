import random
quick_picks = int(input("How many quick picks: "))
for a in range(quick_picks):
    numbers = []
    for i in range(6):
        while len(numbers) < 6:
            random_numbers = random.randint(1, 45)
            if random_numbers in numbers:
                numbers.remove(random_numbers)
            numbers.append(random_numbers)
            numbers.sort()
    for z in numbers:
        print("{:>2}".format(z), end=" ")
    print("")

