R,C,K = map(int,input().split())
N = int(input())
mapListR = [0 for _ in range(R)]
mapListC = [0 for _ in range(C)]
candyListR = [0 for _ in range(K + 1)]
candyListC = [0 for _ in range(K + 1)]
inputList = [[int(i) for i in input().split()] for j in range(N)]

for i,j in inputList:
    i,j = i - 1,j - 1
    mapListR[i] += 1
    mapListC[j] += 1

for i in mapListR:
    if 0 <= i <= K:
        candyListR[i] += 1
for i in mapListC:
    if 0 <= i <= K:
        candyListC[i] += 1
ans = 0

for i,j in inputList:
    i, j = i - 1, j - 1
    if mapListR[i] + mapListC[j] == K:
        ans -= 1
    if mapListR[i] + mapListC[j] == K + 1:
        ans += 1

for i in range(K + 1):
    ans += candyListR[i] * candyListC[K - i]

print(ans)
