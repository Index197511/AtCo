n=int(input())
a=[int(input()) for i in range(n)]
s=sorted(set(a))
d={x:i for i,x in enumerate(s)}
for i in a:
    print(d[i])
