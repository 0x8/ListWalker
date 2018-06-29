"""
Ian Guibas

Custom List type that allows a cyclic look through its contained
elements.
"""

class ListWalker():

    def __init__(self, li):
        self._itemlist = li
        self._len = len(self._itemlist)
        self._iidx = -1
        self._cidx = -1
        self.front = self._itemlist[0]

    def __len__(self):
        return self._len

    def __contains__(self, item):
        if item in self._itemlist:
            return True
        else:
            return False

    def __repr__(self):
        return "ListWalker()"

    def __str__(self):
        return str(self._itemlist)

    def __iter__(self):
        return self

    def __next__(self):
        self._iidx += 1
        if self._iidx == self._len:
            self._iidx = -1
            raise StopIteration
        return self._itemlist[self._iidx]

    def __getitem__(self, index):
        if index < 0:
            if (index * -1) > self._len:
                raise IndexError  # -idx can be == len (somelist[-len(somelist)] == somelist[0])
                                  # but somelist[-len(somelist)-1] shouldn't make sense or work.
            index = self._len + index  # Neg. idx yields len-idx. indexing from right.
        if index >= self._len:
            raise IndexError        
        return self._itemlist[index]

    def show_list(self):
        print(self._itemlist)

    def remove(self, item):
        if item in self._itemlist:
            self._itemlist.remove(item)

    def next(self):

        # On end, cycle to zero
        if self._cidx + 1 == self._len:
            self._cidx = 0
        # Otherwise, simple increment
        else:
            self._cidx = self._cidx+1
        
        return self._itemlist[self._cidx]

    def previous(self):
        
        # On zero, cycle to end
        if self._cidx == 0:
            self._cidx = self._len - 1
        # Otherwise, simple decrement
        else:
            self._cidx = self._cidx - 1

        return self._itemlist[self._cidx]

    def get_idx(self):
        return self._cidx

    def get_items(self):
        return self._itemlist

    def append(self, item):
        ''' add item to the list, requires update of length '''
        self._itemlist.append(item)
        self._len = len(self._itemlist)

    def pop(self,idx=-1):
        item = self._itemlist.pop(idx)
        self._len = len(self._itemlist)
        return item

    def get_front(self):
        return self._itemlist[0]
