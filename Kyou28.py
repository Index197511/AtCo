n,m=map(int,input().split())
p=[]
for i in range(m):
    a,b=map(int,input().split())
    p.append([i,a,b,0])
ps=sorted(p,key=lambda i:(i[1],i[2]))
cnt=1
for i in range(m):
    if i!=0:
        if ps[i][1]==ps[i-1][1]:
            cnt+=1
            ps[i][3]=cnt
        else:
            ps[i][3]=1
            cnt=1
    else:
        ps[i][3]=1
ps=sorted(ps,key=lambda i:i[0])
for i in range(m):
    print("{0:06d}".format(ps[i][1]),end='')#文末の改行取り消し
    print("{0:06d}".format(ps[i][3]))
