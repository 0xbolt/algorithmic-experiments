import numpy as np

def mergesort(arr):
    if len(arr) == 1:
        return arr
    i = len(arr) // 2
    return merge(mergesort(arr[:i]), mergesort(arr[i:]))

def merge(u, v):
    i = 0
    j = 0
    w = []
    while True:
        if i < len(u) and (j == len(v) or u[i] < v[j]):
            w.append(u[i])
            i += 1
        elif j < len(v):
            w.append(v[j])
            j += 1
        else:
            break
    return w

def main():
    arr = np.random.random(10)
    sorted_arr = mergesort(arr)

    arr.sort()
    assert all(arr == sorted_arr)

if __name__ == '__main__':
    main()
