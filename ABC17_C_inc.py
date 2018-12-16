n,m=map(int,input().split())
imos=[0]*(m+10)
total=0
for i in range(n):#Imos法
    l,r,s=map(int,input().split())
    total+=s
    imos[l]+=s
    imos[r+1]-=s
for i in range(m+1):#累積和
    imos[i+1]+=imos[i]
imos=imos[1:m+1]
#全体から累積和の最小値を引いた値を出力
print(total-min(imos))
