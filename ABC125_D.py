n = int(input())
a = list(map(int, input().split()))
count_t = list(filter(lambda x: x < 0, a))
count = len(count_t)
s = []
for i in a:
    if i < 0:
        s.append(i * -1)
    else:
        s.append(i)

if count % 2 == 0 or a.count(0) > 0:
    print(sum(s))
else:
    print(sum(s) - min(s) * 2)
