"""Implementation of the Set ADT container using a Python List"""


class Set:
    """The Set class"""

    def __init__(self):
        """Creates an empty set instance"""
        self._elements = []

    def __len__(self):
        """Returns the lenght of the set"""
        return len(self._elements)

    def __contains__(self, item):
        """returns if an item is in the set"""
        return item in self._elements

    def __iter__(self):
        return _SetIterator(self._elements)

    def add(self, item):
        """Adds a new unique item ot the set"""
        if item not in self._elements:
            self._elements.append(item)

    def remove(self, item):
        """Removes an item from the set"""
        assert item in self._elements, "The item is not in the set"
        self._elements.remove(item)

    def __eq__(self, other):
        """Determines if two sets are equal"""
        if len(self) != len(other):
            return False
        return self.is_subset_of(other)

    def is_subset_of(self, other):
        """Determines if this set is a subset of `other` set"""
        assert len(self) == len(other), "Caridnalities of two sets donot match"
        for item in self:
            if item not in other:
                return False
        return True

    def union(self, other):
        """Creates Union of thwo sets `self` & `other`"""
        new_set = Set()
        new_set._elements.extend(self._elements)
        for item in other:
            if item not in self:
                new_set._elements.append(item)
        return new_set

    def intersection(self, other):
        """Creates an intersection of sets. (A & B)"""
        new_set = Set()
        for item in self:
            if item in other:
                new_set._elements.append(item)
        return new_set

    def difference(self, other):
        """Creates a set difference. (A-B)
        Retruns a new set with items that are in `self` but not in `other`"""
        new_set = Set()
        for item in self:
            if item not in other:
                new_set._elements.append(item)
        return new_set


class _SetIterator:
    """Creates a SetIterator"""

    def __init__(self, elements):
        self._elements = elements
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if 0 <= self._idx < len(self._elements):
            item = self._elements[self._idx]
            self._idx += 1
            return item
        raise StopIteration
