n=int(input())
a=list(map(int,input().split()))
b=[0]*8
free=0
for i in a:
    if 1<=i<400:
        b[0]=1
    elif i<=799:
        b[1]=1
    elif i<=1199:
        b[2]=1
    elif i<=1599:
        b[3]=1
    elif i<=1999:
        b[4]=1
    elif i<=2399:
        b[5]=1
    elif i<=2799:
        b[6]=1
    elif i<=3199:
        b[7]=1
    elif i>=3200:
        free+=1
min_color=8-b.count(0)
if min_color==0 and free!=0:
    min_color=1
max_color=8-b.count(0)
if b.count(0)>free:
    max_color+=free
else:
    max_color=9
print("{} {}".format(min_color,max_color))
