N=int(input())%30
A=[1,2,3,4,5,6]
for i in range(N):
    A[(i%N)],A[(i%N)+1]=A[(i%N)+1],A[(i%N)]
print('{}{}{}{}{}{}'.format(A[0],A[1],A[2],A[3],A[4],A[5]))
