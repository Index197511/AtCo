n=int(input())
a=list(map(int,input().split()))
a.sort()
a.reverse()
for i in range(n-1):
    if a[i]==a[i+1]:
        a[i+1]=0
    else:
        a[i]=0
a.sort()
a.reverse()
print(a[0]*a[1])
