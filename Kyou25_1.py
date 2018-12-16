n=int(input())
a=[]
b=[]
d=[]
c=0
for i in range(n):
    x=int(input())
    a.append(x)
a.sort()
for i in range((len(a)-1)//2):
    d.append(a[-i-1]-a[i])
for i in range(n-1):
    x=a[i+1]-a[i]
    b.append(x)
e=len(b)
c=sum(d)*2
if e%2==1:
    c+=b[e//2]
else:
    c-=min(b[e//2-1],b[e//2])
print(c)
