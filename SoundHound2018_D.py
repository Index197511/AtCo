from scipy.sparse.csgraph import dijkstra
n, m, s, t = map(int, input().split())
ans = 10**15
h = 10**15
snuuk = [[float('inf') for i in range(n)]for j in range(n)]
yen = [[float('inf') for i in range(n)]for j in range(n)]
for i in range(m):
    u, v, a, b = map(int, input().split())
    snuuk[u - 1][v - 1] = b
    snuuk[v - 1][u - 1] = b
    yen[u - 1][v - 1] = a
    yen[v - 1][u - 1] = a
cost_snuuk = dijkstra(snuuk, directed=False, unweighted=False)
cost_yen = dijkstra(yen, directed=False, unweighted=False)
for j in range(n):
    ans = 10**15
    for i in range(n):
        if j <= i:
            ans = min(ans, cost_yen[s - 1][i] + cost_snuuk[i][t - 1])
    print(int(h - ans))
