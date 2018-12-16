N,K=map(int,input().split())
R=list(map(int,input().split()))
ans=0
R=sorted(R)[-K:]
for i in range(K):
    ans=(ans+R[i])/2
print(ans)
