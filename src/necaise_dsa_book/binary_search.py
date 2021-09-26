"""Binary Search Implementation"""


def binary_search(sequence, target):
    """Binary Search Algorithm"""
    ## Step-1: Start with the entire sequence
    low = 0
    high = len(sequence)

    ## Step-2: Repeatedly subdivide the sequence
    while low <= high:
        ## Step-3: Find the middle index
        mid = (low + high) // 2
        ## Step-4: Does the midpoint contain the target?
        if sequence[mid] == target:
            return mid
        elif sequence[mid] > target:
            high = mid - 1  ## Step-5: Or does the target precede the midpoint
        else:
            low = mid + 1  ## Step-6: Or does the target follow the midpoint

    ## Step-7: Finally, return False if the target is not found
    return False
