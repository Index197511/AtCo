import sys
sys.setrecursionlimit(10**6)

def DFS(visit, previous ,color):
    res[visit] = color
    for next in tree[visit]:
        print("visiting = {}, previous = {}, color = {}".format(visit, previous, color))
        if next[0] == previous:
            print("next = {}, previous = {}".format(next[0], previous))
            continue
        if next[1] % 2:
            DFS(next[0], visit, 1-color)
        else:
            DFS(next[0], visit, color)


n = int(input())
tree = [[] for i in range(n)]
res = [0] * n
for i in range(n-1):

    u, v, w = map(int, input().split())
    tree[u-1].append([v-1, w])
    tree[v-1].append([u-1, w])

DFS(0, -1, 1)

for i in range(n):
    print(res[i])
