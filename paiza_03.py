n,m=map(int,input().split())
cnt=0
ans=[]
for i in range(n):
    a,b=map(int,input().split())
    cnt+=1
    if (a-b*5)>=m:
        print(cnt)
