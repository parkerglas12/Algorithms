def selection_sort(arr: list[int]) -> None:
    length: int = len(arr)
    for i in range(length-1):
        min_idx: int = i
        for j in range(i+1, length):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def main() -> None:
    test_list: list[int] = [14, 7, 23, 39, 18, 2, 29, 42, 12, 4]
    selection_sort(test_list)
    print(test_list)

if __name__ == "__main__":
    main()
