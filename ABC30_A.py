a,b,c,d=map(int,input().split())
A=float(b/a)
B=float(d/c)
if A==B:
    print('DRAW')
elif max(A,B)==A:
    print('TAKAHASHI')
elif max(A,B)==B:
    print('AOKI')
