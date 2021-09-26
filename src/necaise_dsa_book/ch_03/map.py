"""Implementation of map ADT using a list"""


class _MapEntry:
    """The the container that holds the `key` & `value` entry for an entry in the map"""

    def __init__(self, key, val):
        """Initializs an instance of this object class"""
        self.key = key
        self.val = val


class Map:
    """The `map` ADT"""

    def __init__(self):
        """Creates an empty map instance"""
        self._entry_list = []

    def __len__(self):
        """Returns the numbe rof entries in the map"""
        return len(self._entry_list)

    def __contains__(self, key):
        """Checks if the map contains the `key`"""
        idx = self._find_position(key)
        return idx is not None

    def _find_position(self, key):
        """Helper method used to find the index position of a category.
        If the key is not found `None` is returned else `index` is returned
        """
        for i, x in enumerate(self._entry_list):
            if x.key == key:
                return i
        return None

    def add(self, key, val):
        """Adds a new entry to the map if the key doesnot exists.
        Otherwise, the new value replaces the current value asociated with the key.
        """
        idx = self._find_position(key)
        print(idx)
        if idx is not None:
            self._entry_list[idx].val = val
            return False
        new_entry = _MapEntry(key, val)
        self._entry_list.append(new_entry)
        return True

    def value_of(self, key):
        """Returns the value stored in `key` entry"""
        idx = self._find_position(key)
        assert idx is not None, "Invalid `key`"
        return self._entry_list[idx].val

    def remove(self, key):
        """Removes the entry associated with `key`"""
        idx = self._find_position(key)
        assert idx is not None, "Invalid `key`"
        self._entry_list.pop(idx)

    def __iter__(self):
        """returns a new iterator on the map `iterable`"""
        return _MapIterator(self._entry_list)


class _MapIterator:
    """Creates a new iterator for map ADT"""

    def __init__(self, entry_list):
        self._entry_list = entry_list
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if 0 <= self._idx < len(self._entry_list):
            item = self._entry_list[self._idx]
            self._idx += 1
            return item
        raise StopIteration
