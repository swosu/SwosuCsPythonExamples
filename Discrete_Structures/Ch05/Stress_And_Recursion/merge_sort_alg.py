from tracker import Tracker

def merge_sort(arr, t: Tracker):
    t.call()
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2; t.add()
    left = merge_sort(arr[:mid], t)
    right = merge_sort(arr[mid:], t)
    return merge(left, right, t)

def merge(left, right, t: Tracker):
    t.call()
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        t.read(); t.read(); t.comp()
        if left[i] <= right[j]:
            result.append(left[i]); t.write(); i += 1; t.add()
        else:
            result.append(right[j]); t.write(); j += 1; t.add()
    result.extend(left[i:]); result.extend(right[j:])
    return result
