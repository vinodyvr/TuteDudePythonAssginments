"""
Write a Python program that:
Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.
"""

Sum: int = 0

for i in range(1,51):
    Sum += i

print(f"The Sum of numbers from 1 to 50 is: {Sum}")
