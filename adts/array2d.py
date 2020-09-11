""" Class Array2D - representing 2D data using a 1D array
"""


class Array2D:
    """ Private inner class _Row - represents a row in the 2D array
    """

    class _Row:
        """ Constructor - represents a row in the 2D array
            Usage:  row = _Row(array2d, row_index)
            @:param array2d the corresponding Array2D that the row belongs to.
            @:param row_index the row index of the row in question
            @:return none
        """

        def __init__(self, array2d, row_index: int) -> None:
            raise NotImplementedError

        """ Bracket operator for getting an item
            Usage: val = array2d[row_index][column_index]
            @:param column_index the desired column_index
            @:return the item at array2d[row_index][column_index]
            @:raises IndexError if the location is out of bounds
        """

        def __getitem__(self, column_index: int):
            raise NotImplementedError

        def __setitem__(self, column_index, data: int):
            raise NotImplementedError

    """ Constructor
        Usage:  array = Array(10)
        @:param size the desired size of the Array
        @:param instance an optional Array2D instance to deep copy data from.
            Should only copy the smaller of the column and row size
        @:return none
        @:raises TypeError if instance is provided and it is not a LinkedList instance
    """

    def __init__(self, row_len: int, column_len: int, instance=None) -> None:
        raise NotImplementedError

    """ Clone the array2d
        Usage:  array2d = Array2D.clone(instance)
        @:param instance an Array instance to deep copy data from.
        @:return a deep object copy of the array2d
    """

    @staticmethod
    def clone(instance):
        raise NotImplementedError

    """ Bracket operator for getting an item
        Usage: val = array2d[row_index][column_index]
        @:param row_index the desired index
        @:return the _Row at the row_index
        @:raises IndexError if the index is out of bounds
    """

    def __getitem__(self, row_index: int):
        raise NotImplementedError

    """ Helper method for getting an item
        Usage: val = array2d.getitem(row_index, column_index)
        @:param row_index the desired row_index
        @:param column_index the desired column_index
        @:return the item at the row_index, column_index
        @:raises IndexError if the index is out of bounds
    """

    def getitem(self, row_index: int, column_index: int):
        raise NotImplementedError

    """ Helper method for setting an item
        Usage: array2d[row_index][column_index] = val
        @:param row_index the desired row_index to set
        @:param column_index the desired column_index to set
        @:param data the desired data to set at indexes
        @:raises IndexError if the index is out of bounds
        @:return none
    """

    def setitem(self, row_index: int, column_index: int, data) -> None:
        raise NotImplementedError

    """ len method for the length of the rows
        Usage: row_length = array2d.get_rows_len()
        @:return the length of the rows
    """

    def get_rows_len(self) -> int:
        raise NotImplementedError

    """ len method for the length of the columns
        Usage: column_length = array2d.get_columns_len()
        @:return the length of the columns
    """

    def get_columns_len(self) -> int:
        raise NotImplementedError

    """ Private helper method for getting the actual index in the 1D array of the item at row_index, column_index
        Usage: actual_index = _get_actual_index(row_index, column_index)
        @:param row_index the desired row_index to set
        @:param column_index the desired column_index to set
        @:raises IndexError if the index is out of bounds
        @:return index the index of the item
    """

    def _get_actual_index(self, row_index: int, column_index: int) -> int:
        raise NotImplementedError

    """ Resize the length of the columns
        Usage: array2d.resize_columns(new_columns_len)
        @:param new_columns_len the desired new length of the columns
        @:raises ValueError if the new_columns_len does not make sense
        @:return none
    """

    def resize_columns(self, new_columns_len: int) -> None:
        raise NotImplementedError

    """ Resize the length of the rows
        Usage: array2d.resize_rows(new_row_len)
        @:param new_rows_len the desired new length of the rows
        @:raises ValueError if the new_rows_len does not make sense
        @:return none
    """

    def resize_rows(self, new_rows_len: int) -> None:
        raise NotImplementedError

    """ Equality operator ==
        Usage: array1 == array2
        @:param other the instance to compare self to
        @:return true if the arrays are equal (deep check)
    """

    def __eq__(self, other) -> bool:
        raise NotImplementedError

    """ Contains operator (in)
        Usage: if 3 in array2d:
        @:param item the desired item to check whether it's in the array
        @:return true if the array contains the item
    """

    def __contains__(self, item) -> bool:
        raise NotImplementedError

    """ Clear the array2d
        Usage: array2d.clear():
        @:return none
    """

    def clear(self) -> None:
        raise NotImplementedError

    """ Return a string representation of the data and structure
        Usage: print(array2d):
        @:return str the string representation of the data and structure
    """

    def __str__(self) -> str:
        raise NotImplementedError
