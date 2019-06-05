n = int(input())
#tree = [[0 for i in range(n)] for i in range(n)]
count = []
tmp = []
#dic = {}
ans = 0
#count = [接続数、cの値、何番目の点]
for i in range(n):
    count.append([0, 0, i])

for i in range(n - 1):
    a, b = map(int, input().split())
    tmp.append([a, b])

    #tree[a-1][b-1], tree[b-1][a-1] = 1, 1
    count[a-1][0] += 1
    count[b-1][0] += 1

c = list(map(int, input().split()))
c.sort(reverse = True)
count.sort()
count.reverse()
#print(count)
for i in range(n):
    count[i][1] = c[i]

count = sorted(count, key = lambda x: x[2])
"""
for i in range(n):
    dic[i] = count[i][1]
"""
print(sum(c) - max(c))
for i in range(n):
    if i == n - 1:
        print(count[i][1])
    else:
        print("{} ".format(count[i][1]), end = "")
