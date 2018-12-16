ans=0
tmp=0
ju=0
cnt=0
h,w,n=map(int,input().split())
#h=height w=width n=amount of cheese
f=[]
for i in range(h):
    a=list(input())
    for j in range(w):
        if a[j]=='S':
            sx,sy=j,i
    f.append(a)
que=[(sy,sx)]
f[sy][sx]=0
f2=f
for g in range(1,n+1):
    while True:
        que_next=[]
        cnt+=1
        for y,x in que:
            for i,j in ((0,1),(1,0),(-1,0),(0,-1)):
                if f2[y+i][x+j]=='.':
                    f2[y+i][x+j]=cnt
                    que.append((y+i,x+j))
                if f2[y+i][x+j]==g:
                    ans+=cnt
                    que=[]
                    que=[(y+i,x+j)]
                    break
                    tmp=g
            if tmp==g:
                break
            else:
                que=que_next
        if tmp==g:
            break
print(ans)
