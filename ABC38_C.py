n=int(input())
a=list(map(int,input().split()))
b=[1]*n
for i in range(1,n):
    if a[i-1]<a[i]:
        b[i]+=b[i-1]
print(sum(b))
