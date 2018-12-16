import itertools
n=int(input())
l=['a','b','c']
h=itertools.product(l,repeat=n)
for i in h:
    print(''.join(i))
