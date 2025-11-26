"""
SET BASICS — EXAMPLE & EXERCISES

EXAMPLE:
Sets store unique items and ignore duplicates.
"""

numbers = {1, 2, 3, 3, 4}
print("Set removes duplicates automatically:", numbers)

# Add item
numbers.add(5)

# Remove item
numbers.remove(2)

# Membership check
print("Is 3 in the set?", 3 in numbers)


"""
YOUR TURN:
1. Create a set of 5 animals.
2. Try adding a duplicate — verify it doesn't change.
3. Remove one animal.
4. Print each animal using a loop.
"""
