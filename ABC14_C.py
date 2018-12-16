#Imos法
n=int(input())
A=[0]*1000002#設けられている制限個数分配列を用意する
a=[]
b=[]
for i in range(n):
    a,b=map(int,input().split())
    A[a]+=1#範囲の始点に1を代入する
    A[b+1]-=1#範囲がｘまでだとすると、+1がなくなるのはその次からでいいのでIndex+1
ans=0
x=0
for i in range(1000002):
    x+=A[i]#累積和を求め、累積和の最大値が答えとなる
    ans=max(ans,x)
print(ans)
