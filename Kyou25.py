n=int(input())
a=[]
hant=0
a1=0
a2=0
st=0
tot=0
flag=0
cnt=0
cnt1=0
for i in range(n):
    a.append(int(input()))
a.sort()
if n%2==0:
    a1=max(abs(a[0]-a[int(n/2)]),abs(a[int(n-1)]-a[int(n/2)]))
    a2=max(abs(a[0]-a[int(n/2)-1]),abs(a[int(n-1)]-a[int(n/2)-1]))
    if a1>=a2:
        st=int(n/2)
    else:
        st=int(n/2)-1
else:
    st=int(n//2)+1
if abs(a[st]-a[0])>=abs(a[st]-a[n-1]):
    for i in range(n):
        if i%2==0:
            tmp=a[-cnt]
            tot+=abs(a[st]+tmp)
            cnt+=1
        else:
            tot+=abs(a[st]-a[cnt1])
            cnt+=1
else:
    for i in range(n):
        if i%2!=0:
            tmp=a[-cnt]
            tot+=abs(a[st]+tmp)
            cnt+=1
        else:
            tot+=abs(a[st]-a[cnt1])
            cnt+=1
print(tot)
