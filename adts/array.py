from adts.iarray import IArray


class Array(IArray):
    def __init__(self, size):
        self._items = [None] * size
        self._size = size

    def __getitem__(self, index):
        pass

    def __setitem__(self, index, data):
        pass

    def __len__(self) -> int:
        pass

    def resize(self, new_size):
        pass

    def __eq__(self, other) -> bool:
        pass

    def __iter__(self):
        pass

    def __delitem__(self, index):
        pass

    def __contains__(self, item) -> bool:
        pass
