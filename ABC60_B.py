a,b,c=map(int,input().split())
for i in range(10**6):
    if (i*b+c)%a==0:
        print("YES")
        exit()
print("NO")
