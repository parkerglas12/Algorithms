# 4. Kaprekar's Routine
# This is a process to explore the behavior of digits in numbers:

# Choose a 4-digit number with at least two distinct digits.
# Arrange its digits in descending and ascending order to create two numbers.
# Subtract the smaller number from the larger one.
# Repeat the process with the result until a constant or loop is reached.
# For example, starting with 6174 leads to a famous constant known as Kaprekar's constant (for 4-digit numbers in base 10).
def kaprekar(n: int) -> int:
    tup: tuple = (int("".join(sorted(digit for digit in str(n)))), int("".join(sorted((digit for digit in str(n)), reverse=True))))
    return max(tup) - min(tup)

print(kaprekar(9378))
    
