n=int(input())
a=[int(i) for i in input().split()]
check=[]
if n%2==0:
    for i in range(1,n,2):
        check+=[i,i]
else:
    check+=[0]
    for i in range(2,n,2):
        check+=[i,i]
if check==sorted(a):
    print((2**(n//2))%(10**9+7))
else:
    print(0)
