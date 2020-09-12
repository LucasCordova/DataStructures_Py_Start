from abc import ABC, abstractmethod

from adts.list_node import ListNode


class ListIterator(ABC):
    """ Class ListIterator - base class representing an iterator to a node in the linked list.
    """

    def __init__(self, node: ListNode) -> None:
        """ Constructor for the ListIterator base class
            Usage:  none - you cannot instantiate a ListIterator directly.
            @:param node the node that the list iterator will point to
            @:return none
            @:raises TypeError if the node provided is None or it is not a ListNode instance
        """
        raise NotImplementedError

    def current(self):
        """ Return the item currently pointed to by the iterator.
            Usage: item = iterator.current()
            @:return item the item stored where the iterator is pointed at
        """
        raise NotImplementedError

    @abstractmethod
    def done(self) -> bool:
        """ Abstract method to return whether the iterator is done.
            Usage: done = iterator.done()
            @:return done boolean that determines whether the iterator is done
        """
        pass

    @abstractmethod
    def move_next(self) -> None:
        """ Abstract method to move the iterator forward or backward.
            Usage: iterator.move_next()
            @:return none
        """
        pass

    @abstractmethod
    def reset(self) -> None:
        """ Abstract method to reset the iterator to beginning or end.
            Usage: iterator.reset()
            @:return none
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """ Abstract method to return a string representation of the data and structure
            Usage: print(iterator):
            @:return str the string representation of the data and structure
        """
        pass
