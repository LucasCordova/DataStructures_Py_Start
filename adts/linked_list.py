from adts.backward_iterator import BackwardIterator
from adts.forward_iterator import ForwardIterator
from adts.list_node import ListNode


class LinkedList:
    """ Class LinkedList - representing an unordered linked list
        Depends on ListNode class to store the items, previous, and next nodes.
    """

    def __init__(self, instance=None) -> None:
        """ Constructor for the LinkedList
            Usage:  linked_list = LinkedList()
            @:param instance an optional instance of a LinkedList to deep copy from
            @:return none
            @:raises TypeError if instance is provided and it is not a LinkedList instance
        """
        raise NotImplementedError

    @staticmethod
    def clone(instance):
        """ Clone the LinkedList
            Usage:  new_linked_list = LinkedList.clone(instance)
            @:param instance a LinkedList instance to deep copy data from.
            @:return a deep object copy of the linked list
            @:raises TypeError if instance is provided and it is not an LinkedList instance
        """
        raise NotImplementedError

    def append(self, item) -> None:
        """ Append an item to the end of the list
            Usage: linked_list.append(item)
            @:param item the desired item to append to the linked list
            @:return none
        """
        raise NotImplementedError

    def prepend(self, item) -> None:
        """ Prepend an item to the end of the list
            Usage: linked_list.prepend(item)
            @:param item the desired item to prepend to the linked list
            @:return none
        """
        raise NotImplementedError

    def insert_before(self, before_item, new_item) -> None:
        """ Insert a new item before a specified item
            Usage: linked_list.insert_before(before_item, new_item)
            @:param before_item the item that the user wishes to insert before
            @:param new_item the desired item to insert
            @:return none
            @:raises KeyError if before_item is not found
        """
        raise NotImplementedError

    def insert_after(self, after_item, new_item) -> None:
        """ Insert a new item after a specified item
            Usage: linked_list.insert_after(after_item, new_item)
            @:param before_item the item that the user wishes to insert before
            @:param new_item the desired item to insert
            @:return none
            @:raises KeyError if before_item is not found
        """
        raise NotImplementedError

    def get_head(self) -> ListNode:
        """ Return the ListNode instance pointing at the head of the linked list.
            Note: this method should be used for debug and test purposes only.
            Usage: head = linked_list.get_head()
            @:return head the ListNode instance representing the head of the linked list
        """
        raise NotImplementedError

    def get_tail(self) -> ListNode:
        """ Return the ListNode instance pointing at the tail of the linked list.
            Note: this method should be used for debug and test purposes only.
            Usage: tail = linked_list.get_tail()
            @:return tail the ListNode instance representing the tail of the linked list
        """
        raise NotImplementedError

    def get_first_item(self):
        """ Return the item at the head of the linked list.
            Usage: first_item = linked_list.get_first_item()
            @:return first_item the item stored in the head of the list
            @:raises IndexError if the list is empty
        """
        raise NotImplementedError

    def get_last_item(self):
        """ Return the item at the tail of the linked list.
            Usage: last_item = linked_list.get_last_item()
            @:return last_item the item stored in the tail of the list
            @:raises IndexError if the list is empty
        """
        raise NotImplementedError

    def clear(self) -> None:
        """ Clear the linked list
            Usage: linked_list.clear():
            @:return none
        """
        raise NotImplementedError

    def forward_begin(self) -> ForwardIterator:
        """ Return a ForwardIterator to the head of the linked list.
            Usage: forward_iterator = linked_list.forward_begin()
            @:return forward_iterator iterator that is pointed to the head of the linked list.
        """
        raise NotImplementedError

    def backward_begin(self) -> BackwardIterator:
        """ Return a BackwardIterator to the tail of the linked list.
            Usage: backward_iterator = linked_list.backward_begin()
            @:return backward_iterator iterator that is pointed to the tail of the linked list.
        """
        raise NotImplementedError

    def extract(self, item):
        """ Extract an item from the Linked List
            @:param item the item to remove
            @:return: None
            @:raises: KeyError if the item is not found
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
            Usage: print(linked_list):
            @:return str the string representation of the data and structure
        """
        raise NotImplementedError
