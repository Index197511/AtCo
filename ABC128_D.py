n, k = map(int, input().split())
v = list(map(int, input().split()))
ans = 0
max_loop = min(k, n)

for left in range(max_loop + 1):
    for right in range(max_loop - left + 1):
        tmp = v[:left] + v[n-right:]
        m = sorted(filter(lambda x: x< 0, tmp))[:k - left - right]
        ans = max(ans, sum(tmp) - sum(m))
print(ans)
