from collections import Counter
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
a=Counter(gubar)
a_mode=a.most_common(1)
b=Counter(gu)
b_mode=b.most_common(1)
if a_mode[0][0]==b_mode[0][0]:
    if gubar.count(a_mode[0][0])<gu.count(b_mode[0][0]):
        ans2=len(gu)-gu.count(b_mode[0][0])
        a_mode=a.most_common(2)
        ans1=len(gubar)-gu.count(a_mode[0][0])
    elif gubar.count(a_mode[0][0])>gu.count(b_mode[0][0]):
        ans1=len(gubar)-gubar.count(a_mode[0][0])
        b_mode=b.most_common(2)
        ans2=len(gu)-gu.count(b_mode[0][0])
    else:
        ans2=n/2
else:
    ans1=len(gubar)-gubar.count(a_mode[0][0])
    ans2=len(gu)-gu.count(b_mode[0][0])
print('{} {}'.format(a_mode[0][0],b_mode[0][0]))
print(int(ans1+ans2))
