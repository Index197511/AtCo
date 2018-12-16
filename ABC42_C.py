N, K = map(int, input().split())
D = list(map(int, input().split()))
n = N
while True:
    i = n
    while i != 0:
        if i % 10 in D:
            break
        i = i // 10
    if i == 0:
        break
    n += 1
print(n)
