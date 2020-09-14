class Pair:
    """ Class Pair - representing a Pair as a Tuple
    """

    def __init__(self, first=None, second=None, instance=None) -> None:
        """ Constructor
            Usage:  pair = Pair('My', 'Pair')
            @:param first the desired first part of the Pair
            @:param second the desired second part of the Pair
            @:param instance an optional Pair instance to deep copy data from.
            @:return none
            @:raises TypeError if instance is provided and it is not a Pair instance
        """
        raise NotImplementedError

    @staticmethod
    def clone(instance):
        """ Clone the pair
            Usage:  pair = Pair.clone(instance)
            @:param instance an Pair instance to deep copy data from.
            @:return a deep object copy of the pair
            @:raises TypeError if instance is provided and it is not an Pair instance
            """
        raise NotImplementedError

    def __getitem__(self, index: int):
        """ Bracket operator for getting an item from the pair. Only [0] and [1] are permitted for index.
            Usage: val = pair[0]
            @:param index the desired index
            @:return the item at the index
            @:raises IndexError if the index is out of bounds
        """
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        """ Equality operator ==
            Usage: pair1 == pair2
            @:param other the instance to compare self to
            @:return true if the pairs are equal (deep check)
        """
        raise NotImplementedError

    def __iter__(self):
        """ Iterator operator
            Usage: for item in pair:
            @:return yields the item at index
        """
        raise NotImplementedError

    def __contains__(self, item) -> bool:
        """ Contains operator (in)
            Usage: if 3 in pair:
            @:param item the desired item to check whether it's in the pair
            @:return true if the pair contains the item
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """ Return a string representation of the data and structure
            Usage: print(pair):
            @:return str the string representation of the data and structure
        """
        raise NotImplementedError
