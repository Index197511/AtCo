import sys
n=int(input())
w=[]
w1=[]
w2=[]
for i in range(n):
    a=input()
    w1.append(a)
    w.append(list(a))
if len(set(w1))!=n:
    print("No")
    sys.exit()
for i in range(n):
    if i==0:
        w2.append(w[i][-1])
    elif i==(n-1):
        w2.append(w[i][0])
    else:
        w2.append(w[i][0])
        w2.append(w[i][-1])
for i in range(0,((n-1)*2),2):
    x=w2[i:2+i]
    if len(set(x))!=1:
        print("No")
        sys.exit()
print("Yes")
