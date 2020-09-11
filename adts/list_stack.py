""" Class ListStack - representing a stack using a LinkedList
"""


class ListStack:
    """ Constructor
        Usage:  stack = ListStack()
        @:param instance an optional ListStack instance to deep copy data from.
        @:return none
        @:raises TypeError if instance is provided and it is not an ListStack instance
    """

    def __init__(self, instance=None) -> None:
        raise NotImplementedError

    """ Clone the stack
        Usage:  stack = ListStack.clone(instance)
        @:param instance an ListStack instance to deep copy data from.
        @:return a deep object copy of the array
    """

    @staticmethod
    def clone(instance):
        raise NotImplementedError

    """ Push an item onto the stack
        Usage:   stack.push(item)
        @:param item to push
        @:return none
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
