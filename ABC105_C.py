n=int(input())
a=''
while (n!=0):
    if n%2==0:
        a='0'+a
        n/=-2
    else:
        a='1'+a
        n-=1
        n/=-2
if(a==""):
    a='0'
print(a)
