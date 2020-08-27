MIN_LENGHT = 4
password = str(input("What is your password: "))
while len(password) < 4:
    print("Password does not meet the minimum requirements")
    password = input("What is your password: ")
for i in range(0, len(password)):
    print("*", end="")
