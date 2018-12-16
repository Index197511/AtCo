a=int(input())
b=int(input())
c=int(input())
first=max(a,b,c)
last=min(a,b,c)
if first==a:
    print('1')
    if b>c:
        print('2')
        print('3')
    else:
        print('3')
        print('2')
elif first==b:
    if a>c:
        print('2')
        print('1')
        print('3')
    else:
        print('3')
        print('1')
        print('2')
else:
    if a>b:
        print('2')
        print('3')
        print('1')
    else:
        print('3')
        print('2')
        print('1')
