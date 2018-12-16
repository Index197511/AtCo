n,q=map(int,input().split())
field=[0 for i in range(n+1)]
for i in range(q):
    l,r=map(int,input().split())
    field[l-1]+=1
    field[r]+=1
ans=[0 for i in range(n)]
ans[0]=field[0]%2
for i in range(1,n):
    ans[i]+=field[i]+ans[i-1]
    ans[i]%=2
print(''.join(map(str,ans)))
