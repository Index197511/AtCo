n,k=map(int,input().split())
a=list(map(int,input().split()))
li=[]
total=0
start=0
cnt=0
ans=0
su=0
for i in range(n):
    total+=a[i]
    cnt+=1
    if cnt>=k:
        su+=total
        total-=a[start]
        start+=1
print(su)
