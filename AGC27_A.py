cnt=0
n,x=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
for i,j in enumerate(a):
    if x>=j:
        x-=j
        cnt+=1
        if i==(n-1) and x>0:
            cnt-=1
print(cnt)
