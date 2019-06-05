import sys
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
cnt=0
tmp=[]
sum_tmp=0
if sum(a)<sum(b):
    print(-1)
    sys.exit()
for i in range(n):
    if a[i]>=b[i]:
        tmp.append(a[i]-b[i])
    else:
        cnt+=1
        sum_tmp+=abs(a[i]-b[i])
tmp.sort(reverse=True)
for i in range(len(tmp)):
    if sum_tmp<=0:
        break
    sum_tmp-=tmp[i]
    cnt+=1

print(cnt)
