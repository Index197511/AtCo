N=int(input())
sum=0
for i in range(N+1):
    sum+=int(i)*10000
ans=sum/N
print(int(ans))
