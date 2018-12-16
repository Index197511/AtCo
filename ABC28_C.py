import itertools
ele=list(map(int,input().split()))
h=itertools.combinations(ele,3)
ad=[]
for i in h:
    ad.append(sum(i))
ans=set(ad)
ans2=sorted(ans,reverse=True)
print(ans2[2])
