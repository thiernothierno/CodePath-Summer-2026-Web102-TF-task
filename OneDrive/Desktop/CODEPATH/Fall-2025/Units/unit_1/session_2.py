# Advanced Problem Set Version 1
# Problem 2: Two-Pointer Reverse List
# This problem will helps student learn one way of implementing the concept of two pointers, and how to use while loop.

# Understanding
# What to return when the given list is empty?
# Is there a time or space complexity constraint?

# Planning
# Return [] when len(lst) is equal to zero.
# Declare two variables low and high pointing at index 0 and len(lst) -1 respectivelly.
# While low < high: do the following:
# Swap elements at position low and high, then increment low by 1 and decrement high by 1.
# Return lst.

# Implementing
def reverse_list(lst):
    """Function that return a reversed list."""
    low = 0
    high = len(lst) - 1
    while low < high:
        tmp = lst[low]
        lst[low] = lst[high]
        lst[high] = tmp
        low += 1
        high -= 1

    return lst


lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
print(reverse_list(lst))


# Problem 4: Sort Array by Parity
# This problem will help student how to distinguish even and odd interger using the modulo division operator.

# Understanding
# Does the given array contain only integers?
# Is there a time or space complexity constraint?
# Does the sorting be in place?
# What to return when the array is empty?

# Planning
# Return [0] if the length of nums is equal to zero.
# Declare two empty arrays evens and odds.
# Iterate over the nums array, for each element check if it remainder equal to 0, then append it to the evens array. Otherwise, append it to the odds array.
# Iterate over the odds array, and append it element to the evens array.
# Return evens array.


# Implementing

def sort_by_parity(nums):
    """Return sorted array by parity"""
    if len(nums) == 0:
        return [0]
    evens = []
    odds = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)

    for odd in odds:
        evens.append(odd)

    return evens


nums = [3, 1, 2, 4]
print(sort_by_parity(nums))

nums = [0]
print(sort_by_parity(nums))
