
name = "Mohamed Yussuf"
age = 27
favourite_language = "Python"
goal = "build real-world applications and master software engineering"

print(f"Hello! My name is {name}.")
print(f"I am {age} years old.")
print(f"My favourite programming language is {favourite_language}.")
print(f"My goal for this course is to {goal}.")
price_input = input("Enter the price of one item: ")
quantity_input = input("Enter the quantity desired: ")

price = float(price_input)
quantity = int(quantity_input)

total = price * quantity

print(f"{quantity} items at {price:.2f} each = {total:.2f}")