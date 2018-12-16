cnt = 0
n, m = map(int, input().split())
dis = [[float('inf') for i in range(n)]for j in range(n)]
tmp = []

for i in range(m):
    tmp.append(list(map(int, input().split())))

for a, b, t in tmp:
    dis[a - 1][b - 1] = t
    dis[b - 1][a - 1] = t

for k in range(n):
    for i in range(n):
        for j in range(n):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

for a, b, t in tmp:
    if t > dis[a - 1][b - 1]:
        cnt += 1

print(cnt)
