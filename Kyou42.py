a,b = map(int, input().split())
if a < 6:
    print(0)
elif a <= 12:
    print(int(b // 2))
else:
    print(b)
