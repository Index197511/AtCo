n,z=map(int,input().split())
a=list(map(int,input().split()))
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
def lcm(a,b):
    return (a*b)//gcd(a,b)
ans=1
for i in a:
    ans=lcm(ans,gcd(z,i))
print(ans)
