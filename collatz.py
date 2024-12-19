def collatz(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    else:
        return n * 3 + 1
    
def main() -> None:
    while True:
        try:
            n: int = int(input("Please enter a positive integer: "))
            if n < 1:
                raise ValueError("Please enter a positive integer.")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            while n != 1:
                n = collatz(n)
                print(n)
            break
    print("The program is done.")

if __name__ == "__main__":
    main()