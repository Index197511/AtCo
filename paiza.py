n=int(input())
a=[]
for i in range(n):
    x=list(input())
    if x[-1]=='s' or x[-1]=='h' and x[-2]=='s' or x[-1]=='o' or x[-1]=='x' or x[-2]=='c' and x[-1]=='h':
        x.append("es")
        a.append("".join(x))
    elif x[-1]=='f':
        b=x.pop()
        x.append("ves")
        a.append("".join(x))
    elif x[-1]=='e' and x[-2]=='f':
        b=x.pop()
        b=x.pop()
        x.append("ves")
        a.append("".join(x))
    elif x[-1]=='y':
        if x[-2]=='a' or x[-2]=='i' or x[-2]=='u' or x[-2]=='e' or x[-2]=='o':
            x.append("s")
            a.append("".join(x))
        else:
            x.pop()
            x.append("ies")
            a.append("".join(x))
    else:
        x.append("s")
        a.append("".join(x))

for i in range(n):
    print(a[i])
