def binary_search(arr: list[int], target: int) -> int | None:
    lo: int = 0
    hi: int = len(arr) - 1
    while lo <= hi:
        mid: int = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return None

def main() -> None:
    test_list: int = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    [print(binary_search(test_list, num)) for num in test_list]

if __name__ == "__main__":
    main()