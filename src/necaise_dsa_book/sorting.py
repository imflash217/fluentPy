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
