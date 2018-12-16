n,s,t=map(int,input().split())
w=0
sum=w
cnt=0
a=[]
for i in range(n):
    a.append(int(input()))
for i in range(n):
    sum+=a[i]
    if s<=sum<=t:
        cnt+=1

print(cnt)
