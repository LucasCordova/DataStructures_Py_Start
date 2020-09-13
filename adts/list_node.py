
class ListNode:
    """ ListNode - represents a node in a linked list
    """

    def __init__(self, item, previous_node=None, next_node=None) -> None:
        """ Constructor - represents a row in the 2D array
            Usage:  node = _Node() or node = _Node(None, None) or node = _Node(previous_node, next_node)
            @:param item the item (data) to store in the node
            @:param previous_node the corresponding previous node of this node in the linked list
            @:param next_node the corresponding next node of this node in the linked list
            @:return none
        """
        raise NotImplementedError

    def get_item(self):
        """ Getter for the item
            Usage: item = node.get_item()
            @:return the item stored in the node
        """
        raise NotImplementedError

    def set_item(self, item) -> None:
        """ Setter for the item
            Usage: node.set_item(item)
            @:param item the item to store in the node
            @:return none
        """
        raise NotImplementedError

    def get_previous_node(self):
        """ Getter for the previous node
            Usage: previous_node = node.get_previous_node()
            @:return the previous node of the node
        """
        raise NotImplementedError

    def set_previous_node(self, previous_node) -> None:
        """ Setter for the previous node
            Usage: node.set_previous_node(previous_node)
            @:param previous_node the node's previous_node instance
            @:return none
        """
        raise NotImplementedError

    def get_next_node(self):
        """ Getter for the next node
            Usage: next_node = node.get_next_node()
            @:return the next node of the node
        """
        raise NotImplementedError

    def set_next_node(self, next_node) -> None:
        """ Setter for the next node
            Usage: node.set_next_node(next_node)
            @:param previous_node the node's previous_node instance
            @:return none
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
            Usage: print(node):
            @:return str the string representation of the data and structure
        """
        raise NotImplementedError
