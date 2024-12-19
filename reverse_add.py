# 2. Reverse and Add
def is_palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]

def reverse_and_add(n: int) -> int:
    str_n: str = str(n)[::-1]
    return int(str_n) + n

def main() -> None:
    while True:
        try:
            n: int = int(input("Please enter a positive integer: ")) 
            if n < 1:
                raise ValueError("Please enter a positive integer.")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            while not is_palindrome(n):
                n = reverse_and_add(n)
                print(n)
            break
    print("You're done with the program.")

if __name__ == "__main__":
    main()