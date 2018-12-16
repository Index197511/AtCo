n,x=map(int,input().split())
a=list(map(int,input().split()))
cnt=0
for i in range(n-1):
    if a[i]+a[i+1]>x:
        cnt+=a[i]+a[i+1]-x
        if a[i]>x:
            a[i+1]=0
        else:
            a[i+1]-=a[i]+a[i+1]-x
print(cnt)
