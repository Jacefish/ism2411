# Module 10 - Inventory List Manager
# ISM 2411

# REFLECTION
# 1. The most surprising thing about Python lists is how easy it is
# to add, remove, and organize items. I did not realize you could
# access items using negative numbers and slices.
#
# 2. At a basketball job, a Python list could help keep track of
# equipment and supplies. Instead of manually checking everything
# in Excel, I could use Python to organize the inventory and count
# how many items are available.


# EXERCISE 1 - Build the list
inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print(inventory)
print(len(inventory))


# EXERCISE 2 - Index practice
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])


# EXERCISE 3 - Slicing
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])


# EXERCISE 4 - Modify
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)


# EXERCISE 5 - Tuple comparison
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("TypeError caught! Tuples cannot be changed after creation.")

print(coords)


# EXERCISE 6 - Average of a list of sales
sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count
best = max(sales)
worst = min(sales)

print("Total:", total)
print("Average:", average)
print("Best:", best)
print("Worst:", worst)


# EXERCISE 7 - Accumulator pattern
prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []

for price in prices:
    discounted.append(round(price * 0.90, 2))

print(prices)
print(discounted)


# EXERCISE 8 - Filter above threshold
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print(high_sales)
print("Count:", len(high_sales))
print("Average:", round(sum(high_sales) / len(high_sales), 2))