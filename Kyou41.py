# l <= x <= rのIDで通る
n,m = map(int, input().split())
tmp = []
tip = [0] * 10 ** 7
ma = 0
for i in range(m):
    x,y = map(int, input().split())
    ma = max(ma, y)
    tip[x] += 1
    tip[y + 1] -= 1

for i in range(1, ma + 1):
    tip[i] += tip[i - 1]

print(tip.count(m))
