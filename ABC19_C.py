N=int(input())
a=list(map(int,input().split()))
a.sort()
s=[]
for i in a:
    while i%2==0:
        i//=2
    s.append(i)
print(len(set(s)))
