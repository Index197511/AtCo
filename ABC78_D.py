n,z,w=map(int,input().split())
a=list(map(int,input().split()))
print(max(abs(a[n-2]-a[n-1]),abs(a[n-1]-w)))
