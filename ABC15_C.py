import itertools
n,k=map(int,input().split())
T=[[int(i) for i in input().split()] for i in range(n)]
S=list(itertools.product(range(k),repeat=n))
for seq in S:
    tmp=0
    for i in range(n):
        tmp=tmp^T[i][seq[i]]
    if tmp==0:
        print("Found")
        exit()
print("Nothing")
