import collections
n=int(input())
v=list(map(int,input().split()))
gu=[]
gubar=[]
ans1=0
ans2=0
gu1=set(gu)
gubar1=set(gubar)
gu1=list(gu1)
gubar1=list(gubar1)
cn1=[]
cn2=[]
qu1=0
qu2=0
for i in range(n):
    if i%2==0:
        gubar.append(v[i])
    else:
        gu.append(v[i])
for i in range(len(gu1)):
    cn1.append(gu.count(gu1[i]))
    if max(cn1)<=gu.count(gu1[i]):
        qu1=gu1[i]
cn1.sort(reverse=True)
for i in range(len(gubar1)):
    cn2.append(gubar.count(gubar1[i]))
    if max(cn2)<=gubar.count(gubar[i]):
        qu2=gubar[i]
cn2.sort(reverse=True)
if qu1 == qu2:
    if cn1[0]<cn2[0]:
        print(n-cn2[0]-cn1[1])
    elif cn1[0]>cn2[0]:
        print(n-cn2[1]-cn1[0])
    else:
        print(int(n/2))
else:
    print(n-cn1[0]-cn2[0])
