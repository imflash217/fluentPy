"""Sparse matrix Implementation using 1D array storage"""


class _MatrixElement:
    """Internal class to represent a single element of the Sparse Matrix"""

    def __init__(self, row, col, val):
        self.row = row
        self.col = col
        self.val = val


class SparseMatrix2D:
    """Sparse matrix implementation using 1D array storage"""

    def __init__(self, num_rows, num_cols):
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._element_list = []
        self.shape = (self._num_rows, self._num_cols)

    def num_rows(self):
        """Returns the number of rows"""
        return self._num_rows

    def num_cols(self):
        """Returns the number of columns"""
        return self._num_cols

    def __getitem__(self, idx_tuple):
        """Returns the value of the element at index position"""
        assert len(idx_tuple) == 2, "Invalid number of indices. Need a tuple of size 2"
        idx = self._find_position(idx_tuple[0], idx_tuple[1])
        if idx is not None:
            return self._element_list[idx].val
        return None

    def __setitem__(self, idx_tuple, scalar):
        """Sets the value of an element in the matrix at position `idx_tuple` to `scalar`"""
        assert len(idx_tuple) == 2, "Invalid number of indices. Needs a tuple of size 2"
        idx = self._find_position(idx_tuple[0], idx_tuple[1])
        if idx is not None:
            if scalar != 0.0:
                self._element_list[idx].val = scalar
            else:
                self._element_list.pop(idx)
        else:
            if scalar != 0.0:
                new_element = _MatrixElement(idx_tuple[0], idx_tuple[1], scalar)
                self._element_list.append(new_element)

    def __add__(self, other: SparseMatrix2D):
        assert self.shape == other.shape, "Matrix shapes not compatible for add op."
        new_matrix = SparseMatrix2D(self.num_rows(), self.num_cols())
        ## duplicate the LHS matrix. The elements are mutable;
        ## so we must create new objects and not simply copy the references
        for element in self._element_list:
            duplicate_element = _MatrixElement(element.row, element.col, element.val)
            new_matrix._element_list.append(duplicate_element)

        for element in other._element_list:
            new_val = new_matrix[element.row, element.col] + element.val
            new_matrix[element.row, element.col] = new_val

    def _find_position(self, row, col):
        """Used to find the index of specific matrix element (row, col) in the list
        of non-zero entries. None is returned if element is not found
        """
        for i, element in enumerate(self._element_list):
            if element.row == row and element.col == col:
                return i
        return None

    def scale_by(self, scalar):
        """Scales every element of the matrix by `scalar`"""
        for element in self._element_list:
            element.val *= scalar
