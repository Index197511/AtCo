n=int(input())
a=['1','2','3','4','5','6']
j=0
k=0
n=n%30
for i in range(n):
    j=i%5
    k=i%5+1
    a[j],a[k]=a[k],a[j]
print(''.join(a))
