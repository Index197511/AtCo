from scipy.sparse.csgraph import dijkstra

n,m,s,g1,g2 = map(int, input().split())
glaph = [[float('inf') for i in range(n)] for i in range(n)]
ans = float('inf')
for i in range(n):
    glaph[i][0] = 0

while True:
    a = list(map(int, input().split()))
    if a.count(0) == 5:
        break
    glaph[a[0]-1][a[1]-1] = a[2]

cost = dijkstra(glaph)

for i in range(n):
    ans = min(ans, cost[s-1][i] + cost[i][g1-1] + cost[i][g2-1])

print(int(ans))
