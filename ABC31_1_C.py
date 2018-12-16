n=int(input())
a=list(map(int,input().split()))
ans=-10**10
for i in range(n):
    sym=-10**10
    sum_aoki_tmp=-10**10
    for j in range(n):
        if(j>i):
            x=a[i:j+1]
        elif(i>j):
            x=a[j:i+1]
        else:
            continue
        taka=x[::2]
        aoki=x[1::2]
        sum_taka=sum(taka)
        sum_aoki=sum(aoki)
        if(sum_aoki>sum_aoki_tmp):
            sum_aoki_tmp=sum_aoki
            sum_taka_tmp=sum_taka
    ans=max(ans,sum_taka_tmp)
print(ans)
