n,m=map(int,input().split())
ans=[]
for i in range(m):
    e=list(map(int,input().split()))
    que=sum(e)
    if que>=0:
        ans.append(que)
print(sum(ans))
