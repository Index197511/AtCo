n=int(input())
a,b=map(int,input().split())
k=int(input())
p=list(map(int,input().split()))
ans=[]
ans.append(a)
ans=ans+p
ans.append(b)
if len(ans)==len(set(ans)):
    print('YES')
else:
    print('NO')
