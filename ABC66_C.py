n=int(input())
a=list(map(int,input().split()))
tmp=sum(a)
tmp1=0
min_tmp=tmp
half=int(tmp/2)
for i in range(n-1):
    tmp1+=a[i]
    min_tmp=min(min_tmp,abs(half-tmp1))
    print("tmp={}".format(tmp1))
    print("reslut={}".format(abs(half-tmp1)))
    print(min_tmp)
print(abs(tmp-min_tmp))
