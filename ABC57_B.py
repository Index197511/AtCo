n,m=map(int,input().split())
ans=1000
a=[]
b=[]
for i in range(n):
    x,y=map(int,input().split())
    a.append(x)
    b.append(y)
for i in range(m):
    c,d=map(int,input().split())
    for j in range(n):
        if ans > (abs(a[j]-c)+abs(b[j]-d)):
            ans=(abs(a[j]-c)+abs(b[j]-d))
            ans1=j+1
    print(ans1)
    ans = 1000
    ans1 = 0
