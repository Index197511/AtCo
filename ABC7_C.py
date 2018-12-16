import sys
cnt=0
r,c=map(int,input().split())
sy,sx=map(int,input().split())
gy,gx=map(int,input().split())
c=[]
for i in range(r):
    a=list(input())
    c.append(a)
c[sy-1][sx-1]=0
que1=[(sy-1,sx-1)]
while True:
    que2=[]
    cnt+=1
    for y,x in que1:
        for i,j in ((0,1),(1,0),(-1,0),(0,-1)):
            if c[y+i][x+j]=='.':
                que2.append((y+i,x+j))
                c[y+i][x+j]=cnt
    que1=que2
    if (gy-1,gx-1) in que2:
        print(cnt)
        sys.exit()
