h,w=map(int,input().split())
a=[]
for i in range(h):
    j=list(input())
    if '#' in j:
        a.append(j)
aa=zip(*[i for i in zip(*a) if '#' in i])
for i in aa:
    print(''.join(i))
