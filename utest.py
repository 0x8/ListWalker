from ListWalker import ListWalker

alist = [1,2,3,4,5,6]
itr = iter(alist)
for i in range(7):
    print(next(itr))

alist = ListWalker(alist)
for i in range(7):
    print(alist.next())


