n=int(input())
ans=100000
for i in range(1,n+1):
    j=int(n/i)
    if j>0:
        ans=min(abs(n-i*j+abs(i-j)),ans)
print(ans)
