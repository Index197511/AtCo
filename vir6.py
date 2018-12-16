n=int(input())
a=list(map(int,input().split()))
ans1=max(a)
a.remove(ans1)
ans2=min(a,key=lambda b:abs(ans1/2-b))
print(ans1,ans2)


x=0
for i in range(n-1):
    if abs(k/2-a[x])>abs(k/2-a[i]):
        x=i
print(ans1,a[x])
