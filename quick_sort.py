def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    pivot: int = arr[len(arr) // 2]
    left: list[int] = [n for n in arr if n < pivot]
    middle: list[int] = [n for n in arr if n == pivot]
    right: list[int] = [n for n in arr if n > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def main() -> None:
    test_list: list[int] = [14, 7, 23, 39, 18, 2, 29, 42, 12, 4]
    print(quick_sort(test_list))
    
if __name__ == "__main__":
    main()

    