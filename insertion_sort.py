def insertion_sort(arr: list[int]) -> None:
    for i in range(1, len(arr)):
        j: int = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

def main() -> None:
    test_list: list[int] = [14, 7, 23, 39, 18, 2, 29, 42, 12, 4]
    insertion_sort(test_list)
    print(test_list)

if __name__ == "__main__":
    main()