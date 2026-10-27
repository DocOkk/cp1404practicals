"""Practise range-based loops and printing stars."""

for number in range(1, 21, 2):
    print(number, end=" ")
print()

# a. Count in tens from 0 to 100.
for number in range(0, 101, 10):
    print(number, end=" ")
print()

# b. Count down from 20 to 1.
for number in range(20, 0, -1):
    print(number, end=" ")
print()

# c. Print the requested number of stars on one line.
number_of_stars = int(input("Number of stars: "))
for number in range(number_of_stars):
    print("*", end="")
print()

# d. Print lines of increasing stars.
number_of_lines = int(input("Number of lines: "))
for number in range(1, number_of_lines + 1):
    print("*" * number)
