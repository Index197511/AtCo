n,d,k=map(int,input().split())
rist=[[int(i) for i in input().split()]for _ in range(d)]
for _ in range(k):
    s,t=map(int,input().split())
    l,r=s,s
    for i in range(d):
        tl,tr=rist[i]
        if tl<l and l<=tr:
            l=tl
        if tl<=r and r<tr:
            r=tr
        if l<=t and t<=r:
            print(i+1)
            break
