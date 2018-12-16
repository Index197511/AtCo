n=int(input())
a=list(map(int,input().split()))
a2=[]
for i in range(n):
    a2.append([a[i],i+1])
a2.sort(reverse=True)
for i in range(n):
    print(a2[i][1])
