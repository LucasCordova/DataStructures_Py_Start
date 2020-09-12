
class ListStack:
    """ Class ListStack - representing a stack using a LinkedList
    """

    def __init__(self, instance=None) -> None:
        """ Constructor
            Usage:  stack = ListStack()
            @:param instance an optional ListStack instance to deep copy data from.
            @:return none
            @:raises TypeError if instance is provided and it is not an ListStack instance
        """
        raise NotImplementedError

    @staticmethod
    def clone(instance):
        """ Clone the stack
            Usage:  stack = ListStack.clone(instance)
            @:param instance an ListStack instance to deep copy data from.
            @:return a deep object copy of the array
        """
        raise NotImplementedError

    def push(self, item):
        """ Push an item onto the stack
            Usage:   stack.push(item)
            @:param item to push
            @:return none
        """
        raise NotImplementedError

    def pop(self):
        """ Pop an item from the stack and return the item
            Usage:   item = stack.pop()
            @:return item that is popped
            @:raises IndexError if the stack is empty
        """
        raise NotImplementedError

    def clear(self) -> None:
        """ Clear the stack
            Usage: stack.clear():
            @:return none
        """
        raise NotImplementedError

    def top(self):
        """ Get the item at the top of the stack
            Usage:   item = stack.top()
            @:return item that is at the top of the stack
            @:raises IndexError if the stack is empty
        """
        raise NotImplementedError

    def size(self) -> int:
        """ Get the size of the number of items on the stack
            Usage:   size = stack.size()
            @:return size the number of items on the stack
        """
        raise NotImplementedError

    def empty(self) -> bool:
        """ Check whether the stack is empty
            Usage:   empty = stack.empty()
            @:return empty boolean as to whether the stack is empty
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """ Return a string representation of the data and structure
            Usage: print(stack):
            @:return str the string representation of the data and structure
        """
        raise NotImplementedError
