import random

def is_sorted(arr: list[int]) -> bool:
    return all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))

def monkey_sort(arr: list[int]) -> list[int]:
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr

def main() -> None:
    test_list: list[int] = [14, 7, 23, 39, 18, 2, 29, 42, 12, 4]
    test_list = monkey_sort(test_list)
    print(test_list)

if __name__ == "__main__":
    main()