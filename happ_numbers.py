def sum_of_squares(n: int) -> int:
    return sum(int(digit) ** 2 for digit in str(n))

def is_happy_number(n: int) -> bool:
    seen: set = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum_of_squares(n)
    return n == 1

def main() -> None:
    while True:
        try:
            n: int = int(input("Enter a positive integer: "))
            if n < 1:
                raise ValueError("Please enter a positive integer.")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            if is_happy_number(n):
                print(f"{n} is a happy number.")
            else:
                print(f"{n} is not a happy number.")
            break

if __name__ == "__main__":
    main()