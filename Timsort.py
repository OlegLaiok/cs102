import random
from typing import List


def get_minrun(n: int):
    r = 0
    while n >= 64:
        r |= n & 1
        n >>= 1
    return n + r


def insertion_sort(arr: list, start: int, end: int) -> List[int]:
    for i in range(start + 1, end + 1):
        elem = arr[i]
        j = i - 1
        while j >= start and elem < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = elem
    return arr


def merge(arr: list, start: int, mid: int, end: int) -> List[int]:
    if mid == end:
        return arr
    first = arr[start : mid + 1]
    last = arr[mid + 1 : end + 1]
    len1 = mid - start + 1
    len2 = end - mid
    ind1 = 0
    ind2 = 0
    ind = start

    while ind1 < len1 and ind2 < len2:
        if first[ind1] < last[ind2]:
            arr[ind] = first[ind1]
            ind1 += 1
        else:
            arr[ind] = last[ind2]
            ind2 += 1
        ind += 1

    while ind1 < len1:
        arr[ind] = first[ind1]
        ind1 += 1
        ind += 1

    while ind2 < len2:
        arr[ind] = last[ind2]
        ind2 += 1
        ind += 1

    return arr


def timsort(arr: list) -> List[int]:
    n = len(arr)
    minrun = get_minrun(n)
    for start in range(0, n, minrun):
        end = min(start + minrun - 1, n - 1)
        arr = insertion_sort(arr, start, end)

    curr_size = minrun
    while curr_size < n:
        for start in range(0, n, curr_size * 2):
            mid = min(n - 1, start + curr_size - 1)
            end = min(n - 1, mid + curr_size)
            arr = merge(arr, start, mid, end)
        curr_size *= 2
    return arr


if __name__ == "__main__":
    a = [random.randint(0, 60) for i in range(140)]
    print("Исходный массив: ", a)
    b = a
    print("Python timsort: ", sorted(b))
    print("My timsort:", timsort(a))
