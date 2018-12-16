from collections import Counter

n, x = map(int, input().split())
dp = ["0"] * (n + 1)
dp[0] = "P"
for i in range(1, n + 1):
    dp[i] = "B" + dp[i - 1] + "P" + dp[i - 1] + "B"
tmp = dp[n] + "P" + dp[::-1]
tmp = tmp[0:x]
tmp_counter = Counter(tmp)
print(tmp_counter['P'])
