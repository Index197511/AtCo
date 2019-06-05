n, k = map(int, input().split())
ans = 0
ans = float(ans)
cnt = 1
for i in range(1, n + 1):
    tmp = i
    tmp2 = 1
    cnt -= 1
    if i == 1:
        while (1):
            tmp2 *= 2
            cnt += 1
            if tmp2 >= k:
                break
    ans += (1 / n) * (1 / 2) ** cnt
    print(ans)
print(ans)
