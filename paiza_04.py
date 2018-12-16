import sympy
n=int(input())
for i in range(n):
    a=input()
    a[::-1]
    x=sympy.Symbol('x')
    ad=0
    for i in a:
        if i!='X':
            i=int(i)
            if i%2!=0:
                ad+=int(a[i])*2
            else:
                ad+=int(a[i])
    ans=list(sympy.solve())
    print([ i for i in ans if 0<=i<=9])
