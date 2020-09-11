from adts.list_iterator import ListIterator
from adts.list_node import ListNode

""" Class BackwardIterator - concrete child class of ListIterator.
"""


class BackwardIterator(ListIterator):
    """ Constructor for the ForwardIterator base class
        Usage:  iterator = ForwardIterator(list_node).
        @:param node the node that the iterator will point to
        @:return none
        @:raises TypeError if the node provided is None or it is not a ListNode instance
    """

    def init(self, node: ListNode) -> None:
        raise NotImplementedError

    """ Return whether the iterator is done. 
        Usage: done = iterator.done()
        @:return done boolean that determines whether the iterator is done
    """

    def done(self) -> bool:
        raise NotImplementedError

    """ Move the iterator forward. 
        Usage: iterator.move_next()
        @:return none
    """

    def move_next(self) -> None:
        raise NotImplementedError

    """ Reset the iterator the beginning. 
        Usage: iterator.reset()
        @:return none
    """

    def reset(self) -> None:
        raise NotImplementedError

    """ Return a string representation of the data and structure
        Usage: print(iterator):
        @:return str the string representation of the data and structure
    """

    def __str__(self) -> str:
        raise NotImplementedError
