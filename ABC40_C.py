n=int(input())
a=list(map(int,input().split()))
ans=[0]*n#ansの中にそれぞれの柱への最短距離を更新していく
ans[1]=abs(a[1]-a[0])
for i in range(2,n):
    ans[i]=min(ans[i-1]+abs(a[i]-a[i-1]),ans[i-2]+abs(a[i]-a[i-2]))
    #1マス前から向かうのがいいか2マス前から向かうのがいいか探索する
print(ans[-1])
