n=int(input())
s=input()
ans=0
ans2=0
for i in s:
    if i=='I':
        ans+=1
    else:
        ans-=1
    ans2=max(ans,ans2)
print(ans2)
