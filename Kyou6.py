import itertools
n,x=map(int,input().split())
a=list(map(int,input().split()))
a.append(0)
comb=list(itertools.combinations_with_replacement(a,n))
ans=[]
for i in comb:
    per=sum(i)
    if per==x:
        if 0 in i:
            ans.append(len(set(i))-1)
        else:
            ans.append(len(set(i)))
if len(ans)==0:
    print(0)
else:
    print(max(ans))
