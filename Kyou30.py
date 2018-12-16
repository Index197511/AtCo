import itertools
n=input()
n2=int(n)
num=['3','5','7']
cnt=0
if n2<357:
    print(0)
    exit()
for i in range(3,len(n)+2):
    for j in itertools.product(num,repeat=i):
        if len(set(j))==3 and int("".join(j))<=n2:
            cnt+=1
print(cnt)
