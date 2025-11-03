from tracker import Tracker

def bubble_sort(arr, t: Tracker):
    t.call()
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            t.read(); t.read(); t.comp()
            if a[j] > a[j + 1]:
                t.write(); t.write()
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
