""" Class HashMap - representing a HashMap (dictionary) where the
    buckets are based on an Array and the chains are based on LinkedLists
"""


class HashMap:
    """ Constructor
        Usage:  hash_map = hash_map(23, hash_function)
        @:param size the desired size of the HashMap
        @:param instance an optional HashMap instance to deep copy data from.
            Should only copy the smaller of size or len(instance) items
        @:return none
        @:raises TypeError if instance is provided and it is not an HashMap instance
    """

    def __init__(self, size: int, instance=None) -> None:
        raise NotImplementedError

    """ Clone the hash map
        Usage:  hash_map = HashMap.clone(instance)
        @:param instance an HashMap instance to deep copy data from.
        @:return a deep object copy of the hash map
    """

    @staticmethod
    def clone(instance):
        raise NotImplementedError

    """ Bracket operator for getting an item value
        Usage: val = array[0]
        @:param key the key of the desired value
        @:return the item value associated with the key
        @:raises IndexError if the key is not present in the hashmap
    """

    def __getitem__(self, key):
        raise NotImplementedError

    """ Bracket operator for inserting a key/value pair into the hash map
        Usage: hash_map[key] = val
        @:param key the desired key set
        @:param value the value associated with the key
        @:raises IndexError if key is already present in the hash map
        @:return none
    """

    def __setitem__(self, key, value) -> None:
        raise NotImplementedError

    """ len operator for getting size of the hash map (number of key/value pairs)
        Usage: length = len(hash_map)
        @:return the size of the hash map
    """

    def __len__(self) -> int:
        raise NotImplementedError

    """ Rehash a hash map
        Usage: hash_map.rehash(new_table_size, new_hash_function)
        @:param new_table_size the desired new table size
        @:param new_hash_function the desired new hash function
        @:return none
    """

    def resize(self, new_table_size: int, new_hash_function) -> None:
        raise NotImplementedError

    """ Equality operator ==
        Usage: hash_map1 == hash_map2
        @:param other the instance to compare self to
        @:return true if the hash maps are equal (deep check)
    """

    def __eq__(self, other) -> bool:
        raise NotImplementedError

    """ Iterator operator
        Usage: for key, value in hash_map:
        @:return yields the key at the index
        @:return yields the value at the index
    """

    def __iter__(self):
        raise NotImplementedError

    """ Delete an item in the hash map. Does not resize the buckets, but does remove the associated chain link.
        Usage: del hash_map[key]
        @:param key the desired key to delete
        @:return none
    """

    def __delitem__(self, key) -> None:
        raise NotImplementedError

    """ Contains operator (in)
        Usage: if 3 in hash_map:
        @:param key the desired key to check whether it's in the hash_map
        @:return true if the hash_map contains the key
    """

    def __contains__(self, key) -> bool:
        raise NotImplementedError

    """ Clear the hash map
        Usage: hash_map.clear():
        @:return none
    """

    def clear(self) -> None:
        raise NotImplementedError

    """ Return a string representation of the data and structure
        Usage: print(hash_map):
        @:return str the string representation of the data and structure
    """

    def __str__(self) -> str:
        raise NotImplementedError

    """ Returns a view object. The view object contains the keys of the dictionary, as a list.
        Usage: keys = hash_map.keys()
        @:return list a list containing the keys of the dictionary
    """

    def keys(self):
        raise NotImplementedError

    """ Returns a view object. The view object contains the values of the dictionary, as a list.
        Usage: values = hash_map.values()
        @:return list a list containing the values of the dictionary
    """

    def values(self):
        raise NotImplementedError

    """ Returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
        Usage: items = hash_map.items()
        @:return items as a tuples in a list of the key/value pairs of the dictionary
    """

    def items(self):
        raise NotImplementedError
