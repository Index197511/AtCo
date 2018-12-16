a=int(input())
b=int(input())
if a==b:
    print('EQUAL')
else:
    print(['LESS','GREATER'][max(a,b)==a])
