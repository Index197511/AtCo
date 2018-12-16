m=10**4+7

def solve(n):
    if n<3:
        return [0,0,1][n-1]
    a,b,c=0,0,1
    for _ in range(3,n):
        a,b,c=b,c,(a+b+c)%m
    return c


print(solve(int(input())))
