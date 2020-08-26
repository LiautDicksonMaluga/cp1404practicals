# name = input("What is your name: ")
# out_files = open("names.txt", "w")
# out_files.write(name)
# out_files.close()
#
# in_files = open("names.txt", "r")
# print("Your name is", in_files.readline())
# in_files.close()

in_files = open("numbers.txt", "r")
count = int(input("How many lines want to add together?: "))
total = 0
for line in range(count):
    number = float(in_files.readline())
    total += number
print(total)
in_files.close()

# in_files = open("numbers.txt", "r")
# number = 0
# for line in in_files:
#     numbers = float(line)
#     number += numbers
# print(number)
# in_files.close()
