"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    menu = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = convert_celsius_to_fahrenheit()
            print(fahrenheit)
        elif choice == "F":
            celsius = convert_fahrenheit_to_celsius()
            print(celsius)
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius_to_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return "Result: {:.2f} F".format(fahrenheit)


def convert_fahrenheit_to_celsius():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return "Results: {:.2f} C".format(celsius)


main()
