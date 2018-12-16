n=int(input())
t,a=map(int,input().split())
h=list(map(int,input().split()))
ans=1000000000
for i in range(n):
    if abs(a-(t-(h[i]*0.006)))<ans:
        ans=abs(a-(t-(h[i]*0.006)))
        ind=i+1
print(ind)
