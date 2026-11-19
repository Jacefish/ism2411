# --- Self-Assessment ---
# Question 1: I learned how to write functions, use loops,
# work with variables, and debug errors in Python.
#
# Question 2: The most challenging part was finding bugs
# in the code and understanding how local variables differ
# from global variables. Testing the code helped me understand.
#
# Question 3: I used ChatGPT to help explain Python concepts
# and understand how to fix errors. I reviewed the code and
# tested it to make sure I understood how it worked.

# --- Exercise 1: calculate_tax ---

def calculate_tax(price, rate):
    return price * rate

print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")


# --- Exercise 2: apply_discount ---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(200, tier):.2f}")


# --- Exercise 3: final_price ---

def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    print(f"After {tier} discount: ${discounted_price:.2f}")
    total = discounted_price + calculate_tax(discounted_price, tax_rate)
    print(f"After tax: ${total:.2f}")
    return total

print(f'final_price(200, "gold", 0.07) = {final_price(200, "gold", 0.07):.2f}')


# --- Exercise 4: Loop + function ---

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 5: Debug First, Then Ask ---

sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1


# --- Exercise 6: Scope experiment ---

x = 100  # Global variable

def double_it():
    x = 999  # Local variable; it does not change global x.
    return x * 2

print(x)           # Prints 100
print(double_it()) # Prints 1998
print(x)           # Still prints 100

# Scope means a variable belongs to the part of the program
# where it is defined. The local x does not change the global x.
