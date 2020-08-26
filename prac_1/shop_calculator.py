TOTAL_PRICE = 0

items = int(input("Number of items: "))
while items <= 0:
    print("Invalid number of items")
    items = int(input("Number of items: "))
for i in range(items):
    price = float(input("Price of item: "))
    TOTAL_PRICE += price
print("Total price for 3 items is $", TOTAL_PRICE)
