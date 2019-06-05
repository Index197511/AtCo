from operator import itemgetter
import sys
import math
input = sys.stdin.readline

n = int(input())
c = [int(input()) for i in range(n)]
tips = []
cnt = 1
ans = 0
c = c * 2

if len(set(c)) == 1:
    print(-1)
    exit()

for i in range(1, 2 * n):
    if c[i-1] == c[i]:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1
ans = max(ans, cnt)

print((ans - 1) // 2 + 1)
