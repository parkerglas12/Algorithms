import random

def bubble_sort(arr: list[int]) -> None:
    length: int = len(arr)
    for i in range(length - 1):
        swapped: bool = False
        for j in range(length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

def selection_sort(arr: list[int]) -> None:
    length: int = len(arr)
    for i in range(length - 1):
        min_idx: int = i
        for j in range(i + 1, length):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr: list[int]) -> None:
    for i in range(1, len(arr)):
        j: int = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

def merge_sort(arr: list[int]) -> None:
    if len(arr) > 1:
        left: list[int] = arr[:len(arr) // 2]
        right: list[int] = arr[len(arr) // 2:]

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

def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    pivot: int = arr[len(arr) // 2]
    left: list[int] = [n for n in arr if n < pivot]
    middle: list[int] = [n for n in arr if n == pivot]
    right: list[int] = [n for n in arr if n > pivot]
    return quick_sort(left) + middle + quick_sort(right)

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

def is_sorted(arr: list[int]) -> bool:
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def monkey_sort(arr: list[int]) -> None:
    while not is_sorted(arr):
        random.shuffle(arr)

def main() -> None:
    random.seed(43)
    test_list: list[int] = [random.randint(0, 100) for _ in range(5)]
    monkey_sort(test_list)
    print(test_list)

if __name__ == "__main__":
    main()