import sys
n,k=map(int,input().split())
s=[]
tmp_a=[]
tmp=0
for i in range(n):
    a,b=map(int,input().split())
    tmp_a.append(a)
    s.append([a,b])#aをb個挿入する
s.sort()
tmp1_a=set(tmp_a)
sS=[]
s_sum=s[0][1]
for i in range(1,n):
    if s[i-1][0]==s[i][0]:
        s_sum+=s[i][1]
    else:
        sS.append([s[i-1][0],s_sum])
        s_sum=0
        s_sum+=s[i][1]
    if i==(n-1):
        sS.append([s[i][0],s_sum])
for i in range(len(tmp1_a)):
    tmp+=sS[i][1]
    if tmp>=k:
        print(sS[i][0])
        break
