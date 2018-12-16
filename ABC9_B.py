import sys
N=int(input())
m=[]
for i in range(N):
    m.append(int(input()))

ans=sorted(m)
ans.reverse()
for i in range(N):
    if ans[i]!=ans[i+1]:
        print(ans[i+1])
        sys.exit()
    else:
        pass
print(ans[0])
    
