""" Class Array - representing 1D data using a List
"""


class Array:
    """ Constructor
        Usage:  array = Array(10)
        @:param size the desired size of the Array
        @:param instance an optional Array instance to deep copy data from.
            Should only copy the smaller of size or len(instance) items
        @:return none
        @:raises TypeError if instance is provided and it is not an Array instance
    """

    def __init__(self, size: int, instance=None) -> None:
        raise NotImplementedError

    """ Clone the array
        Usage:  array = Array.clone(instance)
        @:param instance an Array instance to deep copy data from.
        @:return a deep object copy of the array
    """

    @staticmethod
    def clone(instance):
        raise NotImplementedError

    """ Bracket operator for getting an item
        Usage: val = array[0]
        @:param index the desired index
        @:return the item at the index
        @:raises IndexError if the index is out of bounds
    """

    def __getitem__(self, index: int):
        raise NotImplementedError

    """ Bracket operator for setting an item
        Usage: array[index] = val
        @:param index the desired index to set
        @:param data the desired data to set at index
        @:raises IndexError if the index is out of bounds
        @:return none
    """

    def __setitem__(self, index: int, data) -> None:
        raise NotImplementedError

    """ len operator for getting length of the array
        Usage: for i in range(len(array))
        @:return the length of the Array
    """

    def __len__(self) -> int:
        raise NotImplementedError

    """ Resize an Array
        Usage: array.resize(5)
        @:param new_size the desired new size
        @:return none
    """

    def resize(self, new_size: int) -> None:
        raise NotImplementedError

    """ Equality operator ==
        Usage: array1 == array2
        @:param other the instance to compare self to
        @:return true if the arrays are equal (deep check)
    """

    def __eq__(self, other) -> bool:
        raise NotImplementedError

    """ Iterator operator
        Usage: for item in array:
        @:return yields the item at index
    """

    def __iter__(self):
        raise NotImplementedError

    """ Delete an item in the array. Copies the array contents from index + 1 down
        to fill the gap caused by deleting the item and shrinks the array size down by one
        Usage: del array[0]
        @:param index the desired index to delete
        @:return none
    """

    def __delitem__(self, index: int) -> None:
        raise NotImplementedError

    """ Contains operator (in)
        Usage: if 3 in array:
        @:param item the desired item to check whether it's in the array
        @:return true if the array contains the item
    """

    def __contains__(self, item) -> bool:
        raise NotImplementedError

    """ Clear the array
        Usage: array.clear():
        @:return none
    """

    def clear(self) -> None:
        raise NotImplementedError

    """ Return a string representation of the data and structure
        Usage: print(array):
        @:return str the string representation of the data and structure
    """

    def __str__(self) -> str:
        raise NotImplementedError
