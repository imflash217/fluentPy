"""Various sorting algorithms"""


def bubble_sort(sequence, ascending=True):
    """Sorts a sequence using bubble sort algorithm"""
    n = len(sequence)
    ## Step-1: Perform n-1 bubble ops on the sequence
    for i in range(n - 1):
        ## Step-2: Bubble the larget/smallest element to the end
        for j in range(n - 1 - i):
            if (ascending and sequence[j] > sequence[j + 1]) or (
                not ascending and sequence[j] < sequence[j + 1]
            ):
                ## Swap the j & j+1 items
                tmp = sequence[j]
                sequence[j] = sequence[j + 1]
                sequence[j + 1] = tmp


def selection_sort(sequence, ascending=True):
    """Inplace Sorts a sequence using Selection Sort Algorithm"""
    n = len(sequence)
    for i in range(n - 1):
        ## Step-1: Suppose ith element is the smallest
        pivot = i
        ## Step-2: Determine if any other element contains a smaller value
        for j in range(i + 1, n):
            if (ascending and sequence[j] < sequence[pivot]) or (
                not ascending and sequence[j] > sequence[pivot]
            ):
                pivot = j

        ## Step-3: Swap the ith value and small_idx value
        ## only if the smallest value is not already in its proper position.
        ## Some implementations omit testing the value and always swap
        if pivot != i:
            tmp = sequence[i]
            sequence[i] = sequence[pivot]
            sequence[pivot] = tmp


def insertion_sort(sequence, ascending=True):
    n = len(sequence)
    for i in range(1, n):
        val = sequence[i]
        pivot = i
        while pivot > 0 and (
            (ascending and val < sequence[pivot - 1])
            or (not ascending and val > sequence[pivot - 1])
        ):
            sequence[pivot] = sequence[pivot - 1]
            pivot -= 1
        sequence[pivot] = val


def find_sorted_position(sequence, target, is_ascending=True):
    """Finding the insert position of the target element in a already sorted sequence"""
    low = 0
    high = len(sequence) - 1
    while low < high:
        mid = (low + high) // 2
        if sequence[mid] == target:
            return mid
        elif (is_ascending and target < sequence[mid]) or (
            not is_ascending and target > sequence[mid]
        ):
            ## search in the left half
            high = mid - 1
        elif (is_ascending and target > sequence[mid]) or (
            not is_ascending and target < sequence[mid]
        ):
            ## search in the right half
            low = mid + 1
    print(low, mid, high)
    return low
