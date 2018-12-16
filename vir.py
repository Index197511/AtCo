n=int(input())
a=list(map(int,input().split()))
b=max(a)
a.remove(b)
d=b//2
a1=[]
for i in range(len(a)):
    a1.append(abs(d-a[i]))
c=min(a1)
if d+c in a:
    print("{} {}".format(b,d+c))
else:
    print("{} {}".format(b,d-c))
