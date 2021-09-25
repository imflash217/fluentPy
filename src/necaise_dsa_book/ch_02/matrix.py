"""Implementation of the Matrix ADT using a 2DArray"""

from array import Array2D


class Matrix:
    """The 2D Matrix class"""

    def __init__(self, n_rows, n_cols):
        """Creates a matrix of size = [n_rows, n_cols].
        Initialized to 0.
        """
        self._grid = Array2D(n_rows, n_cols)
        self._grid.clear(0)
        self.shape = self._grid.shape

    def __getitem__(self, idx_tuple):
        """Returns the element of the matrix at position 'idx_tuple'"""
        return self._grid[idx_tuple[0], idx_tuple[1]]

    def __setitem__(self, idx_tuple, val):
        """Sets the value of the element at 'idx_tuple' with a new value 'val'"""
        self._grid[idx_tuple[0], idx_tuple[1]] = val

    def num_rows(self):
        """Returns the number of rows in the matrix"""
        return self._grid.num_rows()

    def num_cols(self):
        """Returns the numbe rof columns in a matrix"""
        return self._grid.num_cols()

    def scale_by(self, scalar):
        """Inplace Multiplies every element of the matrix by the `scalar`"""
        for row in self._grid:
            for element in row:
                element *= scalar

    def transpose(self):
        """Creates and returns a NEW transposed matrix with rows and columns swapped"""
        ...

    def __add__(self, other):
        """Adds two matrices together and returns a new matrix"""
        assert self.shape == other.shape, "Matrix shapes not compatible"
        new_matrix = Matrix(self.shape[0], self.shape[1])
        for r in range(self.shape[0]):
            for c in range(self.shape[1]):
                new_matrix[r, c] = self[r, c] + other[r, c]
        return new_matrix

    def __mul__(self, other: Matrix):
        """Matrix multiples the two matrices. returns a new matrix"""
        assert isinstance(other, Matrix), "the `other` is not a Matrix class instance"
        assert (
            self.shape[1] == other.shape[0]
        ), "Incompatible shapes of the two matrices"
        new_matrix = Matrix(self.shape[0], other.shape[1])
        for r in range(self.shape[0]):
            for c in range(other.shape[1]):
                val = 0
                for i in range(self.shape[1]):
                    val += self[r, i] * other[i, c]
                new_matrix[r, c] = val
        return new_matrix
