x,y=map(int,input().split())
a=[0]*4
b=[]
a[0]=y-x
a[1]=y+x+1
a[2]=-y-x+1
a[3]=-y+x+2
for i in a:
    if i>0:
        b.append(i)
print(min(b))
