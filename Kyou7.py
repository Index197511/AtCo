a=list(map(int,input().split()))
a.sort(reverse=True)
b=int(str(a[0])+str(a[1]))
print(b+a[2])
