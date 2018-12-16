N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())

res = A * N

for k in range(0, N + 1):
  ch = H + k * B
  s = max(0, ((N - k) * E - ch) // (D + E) + 1)
  if s + k <= N:
    res = min(res, A * k + C * s)

print(res)
