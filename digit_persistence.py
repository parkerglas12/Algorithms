import math

def digit_persistence(n: int) -> int:
    return math.prod([int(digit) for digit in str(n)])
    
def main() -> None:
    while True:
        try:
            n: int = int(input("Enter a positive integer: "))
            og_n: int = n
            if n < 1:
                raise ValueError("Please enter a positive integer.")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            persistence: int = 0
            while n > 9:
                n = digit_persistence(n)
                persistence += 1
                print(n)
            break
    print(f"The number {og_n} has a persistence of {persistence}.")

if __name__ == "__main__":
    main()