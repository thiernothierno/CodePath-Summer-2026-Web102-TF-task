
# Advanced Problem Set Version 1
# Problem 7: Eeyore's House
# I picked this problem for two reasons. It helps students learn and understand the concept of divisibility and also how nested loop works.

# Understanding
# The two arrays have the same length?
# What should we do when length of one array or both arrays is 0?
# What should we return when a good pair is not found?
# Is there a time or space complexity constraint?

# Planning
# Return 0, if lenght of one array is equal to zero.
# Declare a variable count that will store the total number of good pairs.
# Iterate over both arrays using a nested loop. For each element in array_1 check if it divisible by each element in array_2 * k.
# If yes, increment count by 1.
# Return count.

# Implementing

def good_pairs(pile1, pile2, k):
    """Function that return total number of good pairs."""
    if len(pile1) == 0 or len(pile2) == 0:
        return 0
    count = 0
    for i in pile1:
        for j in pile2:
            if i % (j * k) == 0:
                count += 1

    return count


pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
print(good_pairs(pile1, pile2, k))

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
print(good_pairs(pile1, pile2, k))


# Advanced Problem Set Version 2
# Problem 1: Words Containing Character

# This problem will helps students understand the concept of indexing and some python methods such as length(), range(), and append().


# Understanding
# What should we return when the given list is empty?
# Is x always a character?
# Does duplicate words be counted as 1?
# Is there a time or space complexity constraint?

# Planning
# Declare a empty list to store the final output.
# Return an empty list if the length of the given list is empty.
# Iterate over the given list of words, for each word check if character x is present.
# If present append it index position to the output list.
# Return output list.

# Implementing
def words_with_char(words, x):
    """Function that return a list of indices representing the words that contain the character x"""
    if len(words) == 0:
        return []
    output = []
    n = len(words)
    for i in range(n):
        if x in words[i]:
            output.append(i)
    return output


words = ["batman", "superman"]
x = "a"
print(words_with_char(words, x))

words = ["black panther", "hulk", "black widow", "thor"]
x = "a"
print(words_with_char(words, x))

words = ["star-lord", "gamora", "groot", "rocket"]
x = "z"
print(words_with_char(words, x))


# Standard Problem Set Version 2:
# Problem 3: Trilogy

# The problem will help students grasp the concept of conditional statement (if, elif, else) and how to use the formated string literals (f-string)

# Understanding
# What should we do when the year parameter is not passed in the function.

# Planning
# Use conditional statement
# If year equal to 2005, print: "Batman Begins."
# elif year equal to 2008, print: "The Dark Knight."
# elif year equal to 2012, print: "The Dark Knight Rises"
# else, print: "Christopher Nolan did not release a Batman movie in year."

# Implementing
def trilogy(year):
    """Function that returns the title of movie of a given year."""
    if year == 2005:
        print("Batman Begins.")
    elif year == 2008:
        print("The Dark Knight.")
    elif year == 2012:
        print("The Dark Knight Rises")
    else:
        print(f"Christopher Nolan did not release a Batman movie in {year}.")


year_1 = 2008
trilogy(year_1)

year_2 = 1998
trilogy(year_2)
