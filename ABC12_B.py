N=int(input())
h=int(N/3600)
N=N-3600*h
m=int(N/60)
N=N-60*m
print('%02d:%02d:%02d'%(h,m,N))
