from collections import Counter
n=int(input())
v=list(map(int,input().split()))
gu=[]
gubar=[]
guc=[]
gubarc=[]
guq=[]
gubq=[]
a=0
b=0
ans1=0
ans2=0
for i in range(n):
    if i%2==0:
        gubar.append(v[i])
    else:
        gu.append(v[i])
for i in range(int(n/2)):
    guq.append(gu[i])
    gubq.append(gubar[i])
    print(''.join(guq))
    if gu[i] in guq:
        pass
    else:
        print(i)
        x1=gu.count(gu[i])
        guc.append(x)
        if max(guc)==x1:
            a=gu[i]
    if gubar[i] in gubq:
        pass
    else:
        print(i)
        y=gubar.count(gubar[i])
        gubarc.append(y)
        if max(gubarc)==y:
            b=gubar[i]
guc.sort(reverse=True)
gubarc.sort(reverse=True)
'''
if a==b:
    if gubarc[0]<guc[0]:
        print(len(gu)-guc[0]+len(gubar)-gubarc[1])
    elif max(gubarc)>max(guc):
        print(len(gu)-guc[1]+len(gubar)-gubarc[0])
    else:
        print(n/2)
else:
    print(n-guc[0]-gubarc[0])
'''
