n,m=map(int,input().split())
ans=10**9
tmp_ans=10**9
prin=0
a=[]
b=[]
for i in range(n):
    x,y=map(int,input().split())
    a.append([x,y])
for i in range(m):
    x,y=map(int,input().split())
    b.append([x,y])
for i in range(n):
    tmp_x=a[i][0]
    tmp_y=a[i][1]
    for j in range(m):
        ans=min((abs(tmp_x-b[j][0])+abs(tmp_y-b[j][1])),ans)
        if tmp_ans!=ans:
            prin=j+1
            tmp_ans=ans
    print(prin)
    ans=10**9
    tmp_ans=10**9
