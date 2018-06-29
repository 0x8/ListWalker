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

>>> alist = ListWalker(alist)
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
>>> 
```
