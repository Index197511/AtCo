n=int(input())
a=list(map(int,input().split()))
cnt=0
for i in range(n):
    while True:
        if a[i]%2!=0 and a[i]%3!=2:
            break
        else:
            cnt+=1
            a[i]-=1
print(cnt)
