print("Hello, Python")

# DataTypes

age = 25               # Integer
height = 5.9          # Float
name = "Alice"        # String
is_student = True     # Boolean 
fruits = ["apple", "banana", "cherry"]  # List
person = {"name": "Bob", "age": 30}      # Dictionary
unique_numbers = {1, 2, 3}               # Set
point = (10, 20)                        # Tuple 

# Loops

for fruit in fruits:
    print(fruit)

for fruit in fruits:
    if fruit == "banana": 
        print(fruit + " is my favorite!")

# Function

def greet(name):
    return "Hello, " + name + "!"

print(greet("Pankaj"))