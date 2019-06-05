from scipy.sparse.csgraph import floyd_warshall
import itertools

n, m, r = map(int, input().split())
v = list(map(int, input().split()))
v = [i - 1 for i in v]


graph = [[float('inf') for i in range(n)] for i in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c

tip_graph = floyd_warshall(csgraph = graph, directed = False, return_predecessors = False)

ans = 10 ** 9
tmp = 0

for i in list(itertools.permutations(v,r)):
    tmp = 0
    for j in range(r-1):
        tmp += tip_graph[i[j]][i[j+1]]
    ans = min(ans, tmp)
print(int(ans))
