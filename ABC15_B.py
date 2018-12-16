import math
n=int(input())
A=list(map(int,input().split()))
bug=0
for i in range(len(A)):
    if A[i]!=0:
        bug+=1
print(math.ceil(sum(A)/bug))
