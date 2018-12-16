n=int(input())
a=[]
ans=0
for i in range(n):
    a.append(int(input()))
kaburi=[x for x in set(a) if a.count(x)>1]
for i in range(len(kaburi)):
    ans+=a.count(kaburi[i])-1
print(ans)
