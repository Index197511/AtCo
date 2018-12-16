n,m=map(int,input().split())
a=[]
b=[]
c=n-m+1
for i in range(n):
    a.append(input())
for i in range(m):
    b.append(input())
ans='No'
for i in range(c):
    for j in range(c):
        flag=0
        for k in range(m):
            if b[k]==a[i+k][j:j+m]:
                flag+=1
        if flag==m:
            ans='Yes'
            break
print(ans)
