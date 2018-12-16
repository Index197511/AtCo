#グラフの全点間の最短距離を求めるアルゴリズムである
n,m=map(int,input().split())

g=[[float("inf") for x in range(n+1)] for y in range(n+1)]
for i in range(1,n+1):
  g[i][i]=0

for i in range(m):
  a,b=map(int,input().split())
  g[a][b]=1
  g[b][a]=1

for i in range(1,n+1):
  for j in range(1,n+1):
    for k in range(1,n+1):
      if g[j][i]+g[i][k] < g[j][k]:#A~CとA~B~Cのどちらが短いかを探索する
        g[j][k]=g[j][i]+g[i][k]

for i in range(1,n+1):
  ans=0
  for j in range(1,n+1):
    if g[i][j]==2:
      ans+=1
  print(ans)
