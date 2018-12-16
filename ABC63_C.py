import sys
n=int(input())
s=[]
ans=0
for i in range(n):
    a=int(input())
    if a%10==0:
        b=1
    else:
        b=0
    s.append([b,a])
ans+=sum(i[1] for i in s)
sS=sorted(s,key=lambda x:(x[0],x[1]))
if ans%10!=0:
    print(ans)
    sys.exit()
for i in range(n):
    if sS[i][0]==0:
        ans-=sS[i][1]
        print(ans)
        sys.exit()
print(0)
