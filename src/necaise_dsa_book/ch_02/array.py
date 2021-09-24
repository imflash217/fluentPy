"""Implements the Array ADT using array capabilities of the `ctypes` module"""

import ctypes


class Array:
    """Creates an array with number of elements = size"""

    def __init__(self, size):
        super().__init__()
        assert size > 0, "Array size must be > 0"
        self._size = size

        ## create the array structure using `ctypes` module
        py_array_type = ctypes.py_object * size
        self._elements = py_array_type()

        ## Initialize each element
        self.clear(None)

    def __len__(self):
        """Returns the size of the Array instance"""
        return self._size

    def __getitem__(self, idx):
        """Returns the element in the array at position 'idx'"""
        assert 0 <= idx < len(self), "Array index Out-Of-Range"
        return self._elements[idx]

    def __setitem__(self, idx, val):
        """Puts the value in the array element at idx position"""
        assert 0 <= idx < len(self), "Array index Out-Of-Range"
        self._elements[idx] = val

    def __iter__(self):
        """Returns the array's iterator for traversing the elements"""
        return _ArrayIterator(self._elements)

    def clear(self, val):
        """Clears the array by setting each element to the given value"""
        for idx in range(len(self)):
            self._elements[idx] = val


class _ArrayIterator:
    """An iterator for the Array ADT"""

    def __init__(self, array):
        self._array = array
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        """Yields the next element of the array iterator"""
        if self._idx < len(self._array):
            item = self._array[self._idx]
            self._idx += 1
            return item
        raise StopIteration
