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
