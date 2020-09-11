from abc import ABC, abstractmethod

from adts.list_node import ListNode

""" Class ListIterator - base class representing an iterator to a node in the linked list.
"""


class ListIterator(ABC):
    """ Constructor for the ListIterator base class
        Usage:  none - you cannot instantiate a ListIterator directly.
        @:param node the node that the list iterator will point to
        @:return none
        @:raises TypeError if the node provided is None or it is not a ListNode instance
    """

    def __init__(self, node: ListNode) -> None:
        raise NotImplementedError

    """ Return the item currently pointed to by the iterator. 
        Usage: item = iterator.current()
        @:return item the item stored where the iterator is pointed at        
    """

    def current(self):
        raise NotImplementedError

    """ Abstract method to return whether the iterator is done. 
        Usage: done = iterator.done()
        @:return done boolean that determines whether the iterator is done
    """

    @abstractmethod
    def done(self) -> bool:
        pass

    """ Abstract method to move the iterator forward or backward. 
        Usage: iterator.move_next()
        @:return none
    """

    @abstractmethod
    def move_next(self) -> None:
        pass

    """ Abstract method to reset the iterator to beginning or end. 
        Usage: iterator.reset()
        @:return none
    """

    @abstractmethod
    def reset(self) -> None:
        pass

    """ Abstract method to return a string representation of the data and structure
        Usage: print(iterator):
        @:return str the string representation of the data and structure
    """

    @abstractmethod
    def __str__(self) -> str:
        pass
