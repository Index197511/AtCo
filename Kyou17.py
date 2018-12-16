import collections
n=int(input())
v=list(map(int,input().split()))
gu=[]
gubar=[]
ans1=0
ans2=0
gu1=set(gu)
gubar1=set(gubar)
cn1=[]
cn2=[]
pro=[]
qu1=0
qu2=0
for i in range(n):
    if i%2==0:
        gubar.append(v[i])
    else:
        gu.append(v[i])
for i in range(2):
    print('{}  {}'.format(gu1[i],gubar1[i]))
    cn1.append(gu.count(gu1[i]))
    cn2.append(gubar.count(gubar1[i]))
'''
y=gu.most_common()[0][0]
x=gubar.most_common()[0][0]
cn1.sort(reverse=True)
cn2.sort(reverse=True)
if len(b)>=1:
    print(n-max(cn1)-max(cn2))
else:
    if max(cn1)<max(cn2):
        print(n-cn2[0]-cn1[1])
    elif max(cn1)>max(cn2):
        print(n-cn2[1]-cn1[0])
    else:
        print(int(n/2))
'''
