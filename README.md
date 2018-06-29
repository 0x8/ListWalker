# ListWalker

A project born of laziness and curiousity, list walker was written to create a
wrapper around lists that can wrap itself cyclicly using the getnext() submethod.

example:

```python  
>>> alist = [1,2,3,4,5,6]
>>> for i in range(7):
...     print(next(itr))
...
1
2
3
4
5
6
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
StopIteration
>>> # Now done with ListWalker
...
>>> alist = ListWalker(alist)
>>> alist
ListWalker([1, 2, 3, 4, 5, 6])
>>> alist.next()
1
>>> alist.next()
2
>>> alist.next()
3
>>> alist.next()
4
>>> alist.reset()
>>> for i in range(7):
...     print(alist.next())
... 
1
2
3
4
5
6
1
>>> alist[0]
1
>>> alist[1]
2
>>> alist[-1]
6
>>> # Proper indexing as well
...
>>> alist[6]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/path/to/ListWalker.py", line 49, in __getitem__
    raise IndexError        
IndexError
>>> alist[-7]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/path/to/ListWalker.py", line 45, in __getitem__
    raise IndexError
IndexError
```
