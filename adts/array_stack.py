""" Class ArrayStack - representing a fixed-size stack using a 1D Array
"""


class ArrayStack:
    """ Constructor
        Usage:  stack = ArrayStack(10)
        @:param size the desired size of the stack
        @:param instance an optional ArrayStack instance to deep copy data from.
            Should only copy the smaller of size or len(instance) items
        @:return none
        @:raises TypeError if instance is provided and it is not an ArrayStack instance
    """

    def __init__(self, size: int, instance=None) -> None:
        raise NotImplementedError

    """ Clone the stack
        Usage:  stack = ArrayStack.clone(instance)
        @:param instance an ArrayStack instance to deep copy data from.
        @:return a deep object copy of the array
    """

    @staticmethod
    def clone(instance):
        raise NotImplementedError

    """ Push an item onto the stack
        Usage:   stack.push(item)
        @:param item to enqueue
        @:return none
        @:raises IndexError if the stack is full
    """

    def push(self, item):
        raise NotImplementedError

    """ Pop an item from the stack and return the item
        Usage:   item = stack.pop()
        @:return item that is popped
        @:raises IndexError if the stack is empty
    """

    def pop(self):
        raise NotImplementedError

    """ Clear the stack
        Usage: stack.clear():
        @:return none
    """

    def clear(self) -> None:
        raise NotImplementedError

    """ Get the item at the top of the stack
        Usage:   item = stack.top()
        @:return item that is at the top of the stack
        @:raises IndexError if the stack is empty
    """

    def top(self):
        raise NotImplementedError

    """ Get the size of the number of items on the stack
        Usage:   size = stack.size()
        @:return size the number of items on the stack
    """

    def size(self) -> int:
        raise NotImplementedError

    """ Check whether the stack is full
        Usage:   full = stack.full()
        @:return full boolean as to whether the stack is full
    """

    def full(self) -> bool:
        raise NotImplementedError

    """ Check whether the stack is empty
        Usage:   empty = stack.empty()
        @:return empty boolean as to whether the stack is empty
    """

    def empty(self) -> bool:
        raise NotImplementedError

    """ Return a string representation of the data and structure
        Usage: print(stack):
        @:return str the string representation of the data and structure
    """

    def __str__(self) -> str:
        raise NotImplementedError
