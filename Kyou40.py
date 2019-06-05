n = int(input())
tree = [[0 for i in range(n)] for i in range(n)]

for i in range(n):
    u, v, w = map(int, input().split())
    tree[u][v] = w
    tree[v][u] = w
