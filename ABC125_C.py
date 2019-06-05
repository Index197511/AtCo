from operator import itemgetter
from functools import reduce
import fractions as f
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
rev_a = list(reversed(a))
ans = 0
accumulation_gcd = [0] * n
rev_accumulation_gcd = [0] * n
accumulation_gcd[0] = a[0]
rev_accumulation_gcd[0] = rev_a[0]

for i in range(1, n):
    accumulation_gcd[i] = f.gcd(a[i], accumulation_gcd[i-1])
    rev_accumulation_gcd[i] = f.gcd(rev_a[i], rev_accumulation_gcd[i-1])

rev_accumulation_gcd.reverse()


for i in range(n):
    if i == 0:
        ans = max(ans, rev_accumulation_gcd[1])
    elif i == (n - 1):
        ans = max(ans, accumulation_gcd[n-2])
    else:
        ans = max(ans, f.gcd(accumulation_gcd[i-1], rev_accumulation_gcd[i+1]))

print(ans)
