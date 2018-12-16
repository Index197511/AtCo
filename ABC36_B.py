n=int(input())
s=reversed([input() for i in range(n)])
for i in zip(*s):
    print(''.join(i))
