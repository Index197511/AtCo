n=int(input())
b = list(map(int,input().split()))
a = []
bb = []
down = []

if n < max(b):
    print(-1)
    exit()


for i in range(n):
    if b[i] > i+1:
        print(-1)
        exit()



a.append(1)
b.remove(1)
bb = list(reversed(b))

for i in range(n-1):
    if len(bb) >= 3:
        a.append(bb[0])
        a.append(bb[2])
        a.append(bb[1])
        del bb[0]
        del bb[0]
        del bb[0]
    else:
        break
for i in range(len(a)):
    print(a[i])

for i in range(len(bb)):
    print(bb[i])
