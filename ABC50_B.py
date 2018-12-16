n=int(input())
t=list(map(int,input().split()))
m=int(input())
ans=[]
for i in range(m):
    p,x=map(int,input().split())
    tot=sum(t)
    tot=tot-t[p-1]+x
    ans.append(tot)
for i in ans:
    print(i)
