n=int(input())
a=list(map(int,input().split()))
cnt=0
for i in range(n):
    tot=0
    j=i
    while True:
        if j==(n-1):
            break
        tot+=a[j]
        if tot==0:
            cnt+=1
        j+=1
        if j==(n-1):
            break
print(int(cnt))
