n=int(input())
x=[]
y=[]
h=[]
x1=[]
y1=[]
x2=[]
y2=[]
x3=[]
y3=[]
tmp=0
for i in range(n):
    x.append(list(map(int,input().split())))
y=sorted(x,key=lambda x:x[2])
y.reverse()
for i in range(n):
    x3.append(y[i][0])
    y3.append(y[i][1])
    if i == 0:
        x1.append(y[i][0])
        y1.append(y[i][1])
        tmp=y[0][2]
    else:
        if tmp == y[i][2]:
                x1.append(y[i][0])
                y1.append(y[i][1])
        else:
            break
    x2=set(x1)
    y2=set(y1)
if len(x2)==1 or len(y2)==1:
    print('{} {} {}'.format(x1[0],y1[0],y[0][2]))
elif len(x2)==2 or len(y2)==2:
    b1=abs(max(x1)-min(x1))
    a1=abs(max(y1)-min(y1))
    if min(x1)-b1 in x3:
        a=max(x1)
    else:
        a=min(x1)
    if min(y1)-a1 in y3:
        b=max(y1)
    else:
        b=min(y1)
    h1=y[0][2]+1
    print('{} {} {}'.format(a,b,h1))
else:
    a=(max(x1)+min(x1))//2
    b=(max(y1)+min(y1))//2
    h1=y[0][2]+1
    print('{} {} {}'.format(a,b,h1))
