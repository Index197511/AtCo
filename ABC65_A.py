import sys
x,y=map(int,input().split())
a=[1,3,5,7,8,10,12]
b=[4,6,9,11]
c=[2]
if x in a:
    if y in a:
        print('Yes')
        sys.exit()
if x in b:
    if y in b:
        print('Yes')
        sys.exit()
if x in c:
    if y in c:
        print('Yes')
        sys.exit()
print('No')
