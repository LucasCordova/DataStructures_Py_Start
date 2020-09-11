from adts.backward_iterator import BackwardIterator
from adts.forward_iterator import ForwardIterator
from adts.list_node import ListNode

""" Class LinkedList - representing an unordered linked list
    Depends on ListNode class to store the items, previous, and next nodes.
"""


class LinkedList:
    """ Constructor for the LinkedList
        Usage:  linked_list = LinkedList()
        @:param instance an optional instance of a LinkedList to deep copy from
        @:return none
        @:raises TypeError if instance is provided and it is not a LinkedList instance
    """

    def __init__(self, instance=None) -> None:
        raise NotImplementedError

    """ Clone the LinkedList
        Usage:  new_linked_list = LinkedList.clone(instance)
        @:param instance a LinkedList instance to deep copy data from.
        @:return a deep object copy of the linked list
    """

    @staticmethod
    def clone(instance):
        raise NotImplementedError

    """ Append an item to the end of the list
        Usage: linked_list.append(item)
        @:param item the desired item to append to the linked list
        @:return none
    """

    def append(self, item) -> None:
        raise NotImplementedError

    """ Prepend an item to the end of the list
        Usage: linked_list.prepend(item)
        @:param item the desired item to prepend to the linked list
        @:return none
    """

    def prepend(self, item) -> None:
        raise NotImplementedError

    """ Insert a new item before a specified item
        Usage: linked_list.insert_before(before_item, new_item)
        @:param before_item the item that the user wishes to insert before
        @:param new_item the desired item to insert
        @:return none
    """

    def insert_before(self, before_item, new_item) -> None:
        raise NotImplementedError

    """ Insert a new item after a specified item
        Usage: linked_list.insert_after(after_item, new_item)
        @:param before_item the item that the user wishes to insert before
        @:param new_item the desired item to insert
        @:return none
    """

    def insert_after(self, after_item, new_item) -> None:
        raise NotImplementedError

    """ Return the ListNode instance pointing at the head of the linked list. 
        Note: this method should be used for debug and test purposes only.
        Usage: head = linked_list.get_head()
        @:return head the ListNode instance representing the head of the linked list
        @:raises IndexError if the list is empty
    """

    def get_head(self) -> ListNode:
        raise NotImplementedError

    """ Return the ListNode instance pointing at the tail of the linked list. 
        Note: this method should be used for debug and test purposes only.
        Usage: tail = linked_list.get_tail()
        @:return tail the ListNode instance representing the tail of the linked list
        @:raises IndexError if the list is empty
    """

    def get_tail(self) -> ListNode:
        raise NotImplementedError

    """ Return the item at the head of the linked list. 
        Usage: first_item = linked_list.get_first_item()
        @:return first_item the item stored in the head of the list
        @:raises IndexError if the list is empty
    """

    def get_first_item(self):
        raise NotImplementedError

    """ Return the item at the tail of the linked list. 
        Usage: last_item = linked_list.get_last_item()
        @:return last_item the item stored in the tail of the list
        @:raises IndexError if the list is empty
    """

    def get_last_item(self):
        raise NotImplementedError

    """ Clear the linked list
        Usage: linked_list.clear():
        @:return none
    """

    def clear(self) -> None:
        raise NotImplementedError

    """ Return a ForwardIterator to the head of the linked list. 
        Usage: forward_iterator = linked_list.forward_begin()
        @:return forward_iterator iterator that is pointed to the head of the linked list.
    """

    def forward_begin(self) -> ForwardIterator:
        raise NotImplementedError

    """ Return a ForwardIterator to the end of the linked list. 
        Usage: forward_iterator = linked_list.forward_end()
        @:return forward_iterator iterator that is pointed to the end of the linked list.
    """

    def forward_end(self) -> ForwardIterator:
        raise NotImplementedError

    """ Return a BackwardIterator to the tail of the linked list. 
        Usage: backward_iterator = linked_list.backward_begin()
        @:return backward_iterator iterator that is pointed to the tail of the linked list.
    """

    def backward_begin(self) -> BackwardIterator:
        raise NotImplementedError

    """ Return a BackwardIterator to the tail of the linked list. 
        Usage: backward_iterator = linked_list.backward_end()
        @:return backward_iterator iterator that is pointed to the beginning of the linked list.
    """

    def backward_end(self) -> BackwardIterator:
        raise NotImplementedError

    """ Return a string representation of the data and structure
        Usage: print(linked_list):
        @:return str the string representation of the data and structure
    """

    def __str__(self) -> str:
        raise NotImplementedError
