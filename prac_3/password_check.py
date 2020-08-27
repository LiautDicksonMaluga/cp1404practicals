def main():
    password = get_password()
    while len(password) < 4:
        print("Password does not meet the minimum requirements")
        password = input("What is your password: ")
    print_asteriks(password)


def print_asteriks(password):
    for i in range(0, len(password)):
        print("*", end="")


def get_password():
    password = str(input("What is your password: "))
    return password


main()