n=int(input())
a=list(map(int,input().split()))
ans=-10000000000
for i in range(n):
    taka_tmp1=-10000000000
    aoki_tmp1=-10000000000
    for j in range(n):
        if j>i:
            b=a[i:j+1]
        elif j<i:
            b=a[j:i+1]
        else:
            continue
        taka=b[::2]
        aoki=b[1::2]
        tmp_taka=sum(taka)
        tmp_aoki=sum(aoki)
        if(tmp_aoki>aoki_tmp1):
            taka_tmp1=tmp_taka
            aoki_tmp1=tmp_aoki
        ans=max(ans,taka_tmp1)
print(ans)
