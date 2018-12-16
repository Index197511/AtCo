import sys
n,m,X,Y=map(int,input().split())
z=0
x=list(map(int,input().split()))
y=list(map(int,input().split()))
for i in range(Y+1):
    if max(x)<i and min(y)>=i and X<i<=Y:
        print('No War')
        sys.exit()
print('War')
