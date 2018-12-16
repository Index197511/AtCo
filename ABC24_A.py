a, b, c, k = map(int, input().split())
s, t = map(int, input().split())
fee = a * s + b * t
if s + t >= k:
    fee -= c * (s + t)
print(fee)
