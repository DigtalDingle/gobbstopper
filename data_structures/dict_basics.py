"""
DICTIONARY BASICS — EXAMPLE & EXERCISES

EXAMPLE:
Working with key-value pairs.
"""

person = {
    "name": "Alice",
    "age": 30,
    "city": "Denver"
}

print("Example dictionary:", person)

# Add a new key
person["job"] = "developer"

# Update a value
person["age"] = 31

# Loop through keys and values
for key, value in person.items():
    print(key, ":", value)


"""
YOUR TURN:
1. Create a dictionary called 'car' with keys:
   - make
   - model
   - year
2. Add a new key called 'color'
3. Print each key/value pair on its own line
"""
