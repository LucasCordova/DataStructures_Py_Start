
class ArrayStack:
    """ Class ArrayStack - representing a fixed-size stack using a 1D Array
    """

    def __init__(self, size: int, instance=None) -> None:
        """ Constructor
            Usage:  stack = ArrayStack(10)
            @:param size the desired size of the stack
            @:param instance an optional ArrayStack instance to deep copy data from.
                Should only copy the smaller of size or len(instance) items
            @:return none
            @:raises TypeError if instance is provided and it is not an ArrayStack instance
        """
        raise NotImplementedError

    @staticmethod
    def clone(instance):
        """ Clone the stack
                Usage:  stack = ArrayStack.clone(instance)
                @:param instance an ArrayStack instance to deep copy data from.
                @:return a deep object copy of the stack
                @:raises TypeError if instance is provided and it is not an ArrayStack instance
        """
        raise NotImplementedError

    def push(self, item):
        """ Push an item onto the stack
                Usage:   stack.push(item)
                @:param item to enqueue
                @:return none
                @:raises IndexError if the stack is full
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

    def full(self) -> bool:
        """ Check whether the stack is full
                Usage:   full = stack.full()
                @:return full boolean as to whether the stack is full
        """
        raise NotImplementedError

    def empty(self) -> bool:
        """ Check whether the stack is empty
                Usage:   empty = stack.empty()
                @:return empty boolean as to whether the stack is empty
        """
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        """ Equality operator ==
            Usage: array1 == array2
            @:param other the instance to compare self to
            @:return true if the arrays are equal (deep check)
            @:raises TypeError if other is not the right type to compare
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """ Return a string representation of the data and structure
                Usage: print(stack):
                @:return str the string representation of the data and structure
        """
        raise NotImplementedError
