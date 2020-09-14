
class ListQueue:
    """ Class ListQueue - representing a queue based on a LinkedList
    """

    def __init__(self, instance=None) -> None:
        """ Constructor
            Usage:  queue = ListQueue()
            @:param instance an optional ListQueue instance to deep copy data from.
            @:return none
            @:raises TypeError if instance is provided and it is not an ListQueue instance
        """
        raise NotImplementedError

    @staticmethod
    def clone(instance):
        """ Clone the queue
            Usage:  queue = ListQueue.clone(instance)
            @:param instance an ListQueue instance to deep copy data from.
            @:return a deep object copy of the queue
            @:raises TypeError if instance is provided and it is not an ListQueue instance
        """
        raise NotImplementedError

    def enqueue(self, item):
        """ Enqueue an item onto the queue
            Usage:   queue.enqueue(item)
            @:param item to enqueue
            @:return none
        """
        raise NotImplementedError

    def dequeue(self):
        """ Dequeue an item from the queue and return the item
            Usage:   item = queue.dequeue()
            @:return item that is dequeued
            @:raises IndexError if the queue is empty
        """
        raise NotImplementedError

    def clear(self) -> None:
        """ Clear the queue
            Usage: array_queue.clear():
            @:return none
        """
        raise NotImplementedError

    def front(self):
        """ Get the item at the front of the queue
            Usage:   item = queue.front()
            @:return item that is in the front
            @:raises IndexError if the queue is empty
        """
        raise NotImplementedError

    def size(self) -> int:
        """ Get the size of the number of items on the queue
            Usage:   size = queue.size()
            @:return size the number of items on the queue
        """
        raise NotImplementedError

    def empty(self) -> bool:
        """ Check whether the queue is empty
            Usage:   empty = queue.empty()
            @:return empty boolean as to whether the queue is empty
        """
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        """ Equality operator ==
            Usage: array1 == array2
            @:param other the instance to compare self to
            @:return true if the arrays are equal (deep check)
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """ Return a string representation of the data and structure
            Usage: print(queue):
            @:return str the string representation of the data and structure
        """
        raise NotImplementedError
