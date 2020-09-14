from adts.list_iterator import ListIterator
from adts.list_node import ListNode


class ForwardIterator(ListIterator):
    """ Class ForwardIterator - concrete child class of ListIterator.
    """

    def init(self, node: ListNode) -> None:
        """ Constructor for the ForwardIterator base class
            Usage:  iterator = ForwardIterator(list_node).
            @:param node the node that the iterator will point to
            @:return none
            @:raises TypeError if the node provided is None or it is not a ListNode instance
        """
        raise NotImplementedError

    def done(self) -> bool:
        """ Return whether the iterator is done.
            Usage: done = iterator.done()
            @:return done boolean that determines whether the iterator is done
        """
        raise NotImplementedError

    def move_next(self) -> None:
        """ Move the iterator forward.
            Usage: iterator.move_next()
            @:return none
        """
        raise NotImplementedError

    def reset(self) -> None:
        """ Reset the iterator the beginning.
            Usage: iterator.reset()
            @:return none
        """
        raise NotImplementedError

    def __iter__(self):
        """ Iterator operator
            Usage: for item in array:
            @:return yields the item at index
        """
        raise NotImplementedError
