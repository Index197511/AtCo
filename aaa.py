n,x=map(int,input().split())
dp=["0"]*n
dp[0]="P"
for i in range(1,n):
    dp[i]="B"+dp[i-1]+"P"+dp[i-1]+"B"
tmp=dp[0:x+1]
tmp="".join(tmp)
print(tmp.count("P"))
