import sys
N,M=map(int,input().split())

for i in range(N+1):
    for j in range(N+1):
        j=j-i
        k=N-i-j
        if i*4+j*3+k*2==M:
            print('{} {} {}'.format(k,j,i))
            sys.exit()
print('-1 -1 -1')
