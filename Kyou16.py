import collections
n=int(input())
v=list(map(int,input().split()))
gu=[]
gubar=[]
ans1=0
ans2=0
for i in range(n):
    if i%2==0:
        gubar.append(v[i])
    else:
        gu.append(v[i])
a=gubar.most_common()
b=gu.most_common()
gu1,gu2=
if gu.most_common()[0][0] == gubar.most_common()[0][0]:
    if gu.most_common()[0][1] < gubar.most_common()[0][1]:
        print(n-gubar.most_common()[0][1]-)
