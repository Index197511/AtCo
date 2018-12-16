l,h=map(int,input().split())
n=int(input())
for i in range(n):
    a=int(input())
    if a<l:
        print(l-a)
    elif h<a:
        print(-1)
    else:
        print(0)
        
