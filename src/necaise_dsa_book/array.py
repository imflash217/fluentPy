"""Implements the Array ADT using array capabilities of the `ctypes` module"""

import ctypes


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


class Array2D:
    """Creates a 2D array of size = [n_rows, n_cols]"""

    def __init__(self, n_rows, n_cols):
        """Creates a 1D array to store the array refrence for every row"""
        self.shape = (n_cols, n_rows)
        self._rows = Array(n_rows)
        for i in range(n_rows):
            self._rows[i] = Array(n_cols)

    def __getitem__(self, idx_tuple):
        """Gets the content of the array at position [i, j]"""
        assert len(idx_tuple) == 2, "Invalid numbe rof array indices"
        idx_row = idx_tuple[0]
        idx_col = idx_tuple[1]
        assert (
            0 <= idx_row < self.num_rows()
        ), "Invalid Row index. Array subscript out-of-range"
        assert (
            0 <= idx_col < self.num_cols()
        ), "Invalid Column index. Array subscript out-of-range"
        row = self._rows[idx_row]
        element = row[idx_col]
        return element

    def __setitem__(self, idx_tuple, val):
        """Sets the element at position [i, j] with value 'val'"""
        assert len(idx_tuple) == 2, "Invalid number of array indices"
        assert 0 <= idx_tuple[0] < self.num_rows(), "Array subscript out-of-range"
        assert 0 <= idx_tuple[1] < self.num_cols(), "Array subscript out-of-range"
        i_r = idx_tuple[0]
        i_c = idx_tuple[1]
        self._rows[i_r][i_c] = val

    def num_rows(self):
        """Returns the numbe rof rows in the 2D array"""
        return len(self._rows)

    def num_cols(self):
        """Returns the number of columns in the array"""
        return len(self._rows[0])

    def clear(self, val):
        """Resets all elements of the array with this value 'val'"""
        for row in self._rows:
            row.clear(val)


class ArrayNd:
    """N-dimensional Array"""

    def __init__(self, *dims):
        assert (
            len(dims) > 1
        ), f"The NdArray must have 2 or more dimensions. Got dims={len(dims)}"
        self._dims = dims
        size = 1  ## total number of elements in the array
        for d in dims:
            assert d > 0, "Dimension index must be > 0"
            size *= d
        self._elements = Array(size)  ## create a 1D array of size
        self._factors = Array(len(dims))  ## 1D array to store the equation factors
        self._compute_factors()

    def num_dims(self):
        """returns the number of dimensions in the array"""
        return len(self._dims)

    def length(self, dim):
        """Returns the length of the array in a given dimension"""
        assert 1 <= dim < len(self._dims), "Dimension component out of range"
        return self._dims[dim - 1]

    def clear(self, val):
        """Clears the array by setting all elements to the given value"""
        self._elements.clear(val)

    def __getitem__(self, idx_tuple):
        """Returns the value of the element stored in the array at `idx_tuple` location"""
        assert len(idx_tuple) == self.num_dims(), "Invalid number of array indices"
        idx = self._compute_index(idx_tuple)
        assert idx is not None, "Array indices out-of-range"
        return self._elements[idx]

    def __setitem__(self, idx_tuple, val):
        """Sets the value of the element at `idx_tuple` to `val`"""
        assert len(idx_tuple) == self.num_dims(), "Invalid number of array indices"
        idx = self._compute_index(idx_tuple)
        assert idx is not None, "Array indices out of range"
        self._elements[idx] = val

    def _compute_index(self, idx_tuple):
        """Compute the index in the 1D Array storage of the NdArray
        from the Nd-index tuple representing the position the NdArray
        """
        offset = 0
        for i, x in enumerate(idx_tuple):
            if x < 0 or x >= self._dims[i]:
                return None
            offset += x * self._factors[i]
        return offset

    def _compute_factors(self):
        """Computes the factors used to calculate the index
        of an element in the 1D representation of Nd Array
        """
        self._factors[-1] = 1
        i = self.num_dims() - 1
        while i > 0:
            self._factors[i - 1] = self._factors[i] * self._dims[i]
            i -= 1
