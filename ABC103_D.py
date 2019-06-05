n, m = map(int, input().split())
pair = []
ans = 0
x = 0

for i in range(m):
    a, b = map(int, input().split())
    pair.append([a, b])

pair = sorted(pair, key = lambda x: x[1])


for (i,j) in pair:
    if i > x:
        x = j - 1
        ans += 1

print(ans)
