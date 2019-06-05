from operator import itemgetter
import sys
import fractions as f
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = 0

for i in range(n):
