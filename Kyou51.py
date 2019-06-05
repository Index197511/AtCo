n = int(input())

adjacent = [[0] for i in range(n)]
tips = [0] * n
query = []
ans = 0

for i in range(n-1):
    a, b = map(int, input().split())
    adjacent[a-1].append(b-1)
    adjacent[b-1].append(a-1)
    query.append([a-1, b-1])

c = list(map(int, input().split()))
c.sort()
ans = sum(c) - max(c)

for i in adjacent:
    for j in i:
        if tips[j] == 0:
            tips[j] = c.pop()

print(ans)

for i in tips:
    print("{} ".format(i), end = "")

print("\n")
