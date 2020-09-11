""" Class ListQueue - representing a queue based on a LinkedList
"""


class ListQueue:
    """ Constructor
        Usage:  queue = ListQueue()
        @:param instance an optional ListQueue instance to deep copy data from.
        @:return none
        @:raises TypeError if instance is provided and it is not an ListQueue instance
    """

    def __init__(self, instance=None) -> None:
        raise NotImplementedError

    """ Clone the queue
        Usage:  queue = CircularArrayQueue.clone(instance)
        @:param instance an CircularArrayQueue instance to deep copy data from.
        @:return a deep object copy of the array
    """

    @staticmethod
    def clone(instance):
        raise NotImplementedError

    """ Enqueue an item onto the queue
        Usage:   queue.enqueue(item)
        @:param item to enqueue
        @:return none
    """

    def enqueue(self, item):
        raise NotImplementedError

    """ Dequeue an item from the queue and return the item
        Usage:   item = queue.dequeue()
        @:return item that is dequeued
        @:raises IndexError if the queue is empty
    """

    def dequeue(self):
        raise NotImplementedError

    """ Clear the queue
        Usage: array_queue.clear():
        @:return none
    """

    def clear(self) -> None:
        raise NotImplementedError

    """ Get the item at the front of the queue
        Usage:   item = queue.front()
        @:return item that is in the front
        @:raises IndexError if the queue is empty
    """

    def front(self):
        raise NotImplementedError

    """ Get the size of the number of items on the queue
        Usage:   size = queue.size()
        @:return size the number of items on the queue
    """

    def size(self) -> int:
        raise NotImplementedError

    """ Check whether the queue is empty
        Usage:   empty = queue.empty()
        @:return empty boolean as to whether the queue is empty
    """

    def empty(self) -> bool:
        raise NotImplementedError

    """ Return a string representation of the data and structure
        Usage: print(queue):
        @:return str the string representation of the data and structure
    """

    def __str__(self) -> str:
        raise NotImplementedError