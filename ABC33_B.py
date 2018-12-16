import sys
n=int(input())
S=[]
P=[]
for i in range(n):
    s,p=input().split()
    S.append(s)
    P.append(int(p))
tot=sum(P)
for i in range(n):
    if P[i]>tot/2:
        print(S[i])
        sys.exit()
print('atcoder')
