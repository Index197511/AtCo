import sys
N=int(input())
ng=[int(input()) for i in range(3)]
if N in ng:
    print('NO')
    sys.exit()
for i in range(100):
    if (N-3) not in ng:
        N-=3
    elif (N-2) not in ng:
        N-=2
    elif (N-1) not in ng:
        N-=1
    else:
        print('NO')
        sys.exit()
if N>0:
    print('NO')
else:
    print('YES')
