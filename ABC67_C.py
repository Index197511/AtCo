n=int(input())
a=list(map(int,input().split()))
tmp=[]
all_sum=sum(a)
tmp_sum=0
tmp_sum2=all_sum
for i in range(n-1):
    tmp_sum+=a[i]
    tmp_sum2-=a[i]
    tmp.append(abs(tmp_sum-tmp_sum2))
print(min(tmp))
