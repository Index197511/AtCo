n,a,b=map(int,input().split())
point=0
for i in range(n):
    s,d=input().split()
    d=int(d)
    if s=='West':
        if d<a:
            point+=a
        elif a<=d<=b:
            point+=d
        else:
            point+=b
    else:
        if d<a:
            point-=a
        elif a<=d<=b:
            point-=d
        else:
            point-=b
if point<0:
    print('East {}'.format(abs(point)))
elif point>0:
    print('West {}'.format(abs(point)))
else:
    print(0)
