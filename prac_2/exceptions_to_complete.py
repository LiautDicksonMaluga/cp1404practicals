finished = False
result = 0
while not finished:
    try:
        integar = int(input("Please enter a valid integer: "))
        result += integar
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
    print("Valid result is:", result)