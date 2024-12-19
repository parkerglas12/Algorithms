def bubble_sort(arr: list[int]) -> None:
    length: int = len(arr)
    for i in range(length-1):
        swapped: bool = False
        for j in range(length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

def main() -> None:
    test_list: list[int] = [14, 7, 23, 39, 18, 2, 29, 42, 12, 4]
    bubble_sort(test_list)
    print(test_list)

if __name__ == "__main__":
    main()