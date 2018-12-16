N=int(input())
tip=2025-N
for i in range(0,10):
    for j in range(0,10):
        if i*j==tip:
            print('{} x {}'.format(i,j))
