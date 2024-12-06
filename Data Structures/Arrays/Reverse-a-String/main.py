# Create a function that reverse a string.
# Example: "What is your name?"
# Output Example: "?eman ruoy si tahw"


# =========================================================================================
# Example 1:
# taking a function called reverse
def reverse(string):
    # checking input
    # checking if the string empty, has 1 character or less, is an instance of string
    if not string or len(string) < 2 or not isinstance(string, str):
        return "Invalid"

    # taking an empty array
    backward = []
    # total item with index
    total_item = len(string) - 1
    # taking a loop, starting from the last index to 0, decreasing by 1 step
    for x in range(total_item, -1, -1):
        # appending the item of string in backward array
        backward.append(string[x])

    # converting the array into the string with join method
    reverse_string = "".join(backward)

    return reverse_string


print(reverse("What is your name?"))


# Time Complexity: O(n) --> there is a loop and the join method that also iterates.
# =========================================================================================


# =========================================================================================
# Example 2:

# taking a reverse function
def reverse2(string):
    # checking input
    # checking if the string empty, has 1 character or less, is an instance of string
    if not string or len(string) < 2 or not isinstance(string, str):
        return "Invalid"

    # converting string into array/list
    input_array = list(string)

    # reversing the array
    input_array.reverse()

    # converting the array into string
    reverse_string = "".join(input_array)

    return reverse_string


print(reverse2("What is your name?"))

# Time Complexity: O(n) --> reverse method and join method do iterations.
# =========================================================================================
