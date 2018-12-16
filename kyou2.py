import sys
n=int(input())
w=[]
ini=[]
for i in range(n):
    w.append(input())
    s=list(w[i])
    if i==0:
        ini.append(s[-])
    elif i==(n-1):
        ini.append(s[:1])
    else:
        ini.append(s[:1])
        ini.append(s[-1:])
print(''.join(ini))
an=set(ini)
if len(an)!=(n-1):
    print('No')
a=set(w)
if len(a)!=n:
    print('No')
    sys.exit()
else:
    print('Yes')
