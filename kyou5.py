import sys
n=int(input())
w=[]
ini=[]
head=0
heap=0
for i in range(n):
    s=input()
    w.append(s)
    if i!=0:
        head=s[:1]
    elif i==(n-1):
        heap=s[-1:]
    else:
        head=s[:1]
        heap=s[-1:]
    if i!=0:
        print(head)
        print(heap)
        if head==heap:
            pass
        else:
            print('No')
            sys.exit()
if set(w)!=n:
    print('No')

print('Yes')
