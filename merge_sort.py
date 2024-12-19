def merge_sort(arr: list[int]) -> None:
    if len(arr) > 1:
        right: list[int] = arr[len(arr) // 2:]
        left: list[int] = arr[:len(arr) // 2]

        merge_sort(left)
        merge_sort(right)

        i: int = 0
        j: int = 0
        k: int = 0

        while len(left) > i and len(right) > j:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while len(left) > i:
            arr[k] = left[i]
            i += 1
            k += 1

        while len(right) > j:
            arr[k] = right[j]
            j += 1
            k += 1

def main() -> None:
    test_list: list[int] = [14, 7, 23, 39, 18, 2, 29, 42, 12, 4]
    merge_sort(test_list)
    print(test_list)

if __name__ == "__main__":
    main()