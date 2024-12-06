# Python Arrays

# Example

consonant = ["a", "b", "c"]
print(consonant[2])

# ***************************************************************
# Adding an item in Array
# Append method

consonant.append("d")
print(consonant)

# Example 2:
cars = ["Honda", "Tata", "BMW"]
bikes = ["Suzuki", "Bajaj", "Yamaha"]
cars.append(bikes)

print(cars)
# Time complexity: O(1) --> Adding item at the end. No Loop
# ***************************************************************


# ***************************************************************
# Pop
# Example 1
nation = ["Bangladesh", "India", "Pakistan"]
nation.pop()
print(nation)
# Time complexity : O(1) --> Removing the last item. No Loop

# Example 2
number = [1, 2, 3, 4]
number.pop(2)
print(number)
# Time complexity : O(n) --> Removing item at a specific position and shifting index with loop.
# ***************************************************************

# ***************************************************************
# Insert
# Example 1
city = ["Dhaka", "Chittagong", "Mymensingh"]
city.insert(0, "Khulna")
print(city)
# Time complexity: 0(n) --> Adding an item at the beginning shifted other item's indexes with looping.

# Example 2: Add an item in the middle of an Array

fruits = ["Mango", "Jack fruit", "Litchi", "Banana"]
fruits.insert(1, "Orange")
print(fruits)
# Time Complexity: O(n) --> Iteration happened to shifting indexes
# ***************************************************************

