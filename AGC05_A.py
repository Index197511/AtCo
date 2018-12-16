import sys
x=input()
tmp=x.split("ST")
tmp=''.join(tmp)
a=len(tmp)
for i in range(100000):
    tmp=tmp.split("ST")
    tmp=''.join(tmp)
    if len(tmp)==a:
        print(len(tmp))
        break
    elif len(tmp)==0:
        print(0)
        break
    else:
        a=len(tmp)
