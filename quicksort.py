import numpy as np

def quicksort(arr):
    _quicksort(arr, 0, len(arr))
    return arr

def _quicksort(arr, i, j):
    if j - i <= 1:
        return

    pivot = np.random.randint(i, j)
    swap(arr, j - 1, pivot)

    k = i; l = i
    while k < j - 1:
        if arr[k] < arr[j - 1]:
            swap(arr, k, l)
            l += 1
        k += 1
    swap(arr, l, j - 1)
    _quicksort(arr, i, l)
    _quicksort(arr, l + 1, j)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def main():
    arr = np.random.random(20)
    quicksort(arr)
    print(arr)

if __name__ == '__main__':
    main()
