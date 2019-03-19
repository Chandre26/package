def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''

    length = len(items) - 1

    while length >= 0:
        for i in range(length):
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]
        length -= 1
    return items

def merge_sort(items):

    '''Return array of items, sorted in ascending order'''

    if len(items) == 1:
        return items

    mid = len(items)//2
    lower = merge_sort(items[:mid])
    upper = merge_sort(items[mid:])

    return merge(lower, upper)

def merge(A, B):

        result = []

        while len(A) > 0 and len(B) > 0:

            if A[0] < B[0]:
                result.append(A.pop(0))
            else:
                result.append(B.pop(0))

        if len(A) == 0:
            result = result + B
        if len(B) == 0:
            result = result + A

        return result



def quick_sort(items):

    '''Return array of items, sorted in ascending order'''

    low = []
    high = []
    pivot_list = []

    if len(items) <= 1:
        return items

    pivot = items[-1]

    for i in items:
        if i < pivot:
            low.append(i)
        elif i > pivot:
            high.append(i)
        else:
            pivot_list.append(i)

        low = quick_sort(low)
        high = quick_sort(high)

        return less + pivot_list + more
