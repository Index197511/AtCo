import sys
from operator import itemgetter
#UnionFind
input = sys.stdin.readline
class UnionFind:
    def __init__(self, n):

        self.parent = [-1 for _ in range(n)]


    def root(self, x):

        if self.parent[x] < 0:
            return x
        self.parent[x] = self.root(self.parent[x])
        return self.parent[x]


    def merge(self, x, y):

        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.parent[x] > self.parent[y]:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        return True

    def issame(self, x, y):

        return self.root(x) == self.root(y)

n, m = map(int, input().split())
uf = UnionFind(n)
e = []
ans = []
cnt = 0
for i in range(m):
    a, b, c = map(int, input().split())
    e.append([a, b, c, i + 1])
e.sort(key = itemgetter(2), reverse = True)

for i in range(m):
    if cnt == n - 1:
        break
    if not uf.issame(e[i][0] - 1, e[i][1] - 1):
        uf.merge(e[i][0] - 1, e[i][1] - 1)
        ans.append(e[i][3])
        cnt += 1
ans.sort()
for i in ans:
    print(i)
