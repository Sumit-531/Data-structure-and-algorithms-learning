# Rule 2: Drop the constant

def print_first_item_then_first_half_then_say_hi_100_times(items):
    print(items[0])  # O(1)

    middle_index = len(items) / 2
    index = 0

    while index < middle_index:  # O(n/2)
        print(items[index])
        index += 1

    for i in range(100):  # O(100)
        print("hi")

        
# Big O = O(1 + n/2 + 100)
# After applying rule 2 (drop the constant)
# Big O = O(n)


