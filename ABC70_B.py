a,b,c,d=map(int,input().split())
print([0,min(b,d)-max(a,c)][max(a,c)<=min(b,d)])
