n,q=map(int,input().split())
field=[0 for i in range(n+1)]
for i in range(q):
    l,r=map(int,input().split())
    field[l-1]+=1
    field[r]-=1
for i in range(n):
    if i>0:
        field[i]+=field[i-1]
    print(field[i]%2,end='')
print()
