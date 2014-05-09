polist, partially ordered list
=========

.. sourcecode:: python

    >>> from polist import PartialOrderedList
    >>> p = PartialOrderedList()
    >>> p.append(0, 'A')
    >>> p.append(1, 'B')
    >>> p.append(2, 'A')
    >>> p
    [0, 1, 2]
    >>> assert [0, 1, 2] == p
    >>> assert [2, 1, 0] == p
    >>> assert [0, 2, 1] != p
    >>> assert [1, 0, 2] != p
    >>> assert [1, 2, 0] != p
    >>> assert [2, 0, 1] != p
    
    >>> p = PartialOrderedList()
    >>> p.append(0, 'A')
    >>> p.append(1, 'A')
    >>> p.append(2, 'B')
    >>> p.append(3, 'B')
    >>> p.append(4, 'C')
    >>> p.append(5, 'C')
    >>> p
    [0, 1, 2, 3, 4, 5]
    >>> assert [0, 1, 2, 3, 4, 5] == p
    >>> assert [0, 1, 3, 2, 4, 5] == p
    >>> assert [1, 0, 2, 3, 4, 5] == p
    >>> assert [1, 0, 3, 2, 4, 5] == p
    >>> assert [0, 1, 2, 3, 5, 4] == p
    >>> assert [0, 1, 3, 2, 5, 4] == p
    >>> assert [1, 0, 2, 3, 5, 4] == p
    >>> assert [1, 0, 3, 2, 5, 4] == p
