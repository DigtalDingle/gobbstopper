"""
PHONEBOOK MINI-PROJECT

EXAMPLE:
A simple phonebook stored in a dictionary.
"""

phonebook = {
    "Alice": "555-1234",
    "Bob": "555-5678"
}

# Lookup a number
print("Alice's number:", phonebook["Alice"])

# Add a new contact
phonebook["Charlie"] = "555-0000"

# Loop through contacts
for name, number in phonebook.items():
    print(name, "→", number)


"""
YOUR TURN:
1. Create your own phonebook with 3 names.
2. Add two new people.
3. Update one number.
4. Print all contacts alphabetically by name.
"""
