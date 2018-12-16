n=int(input())
x=1
n=str(bin(n))
n=list(n)
a=n.count('1')
if a%2!=0:
    print('Aoki')
else:
    print('Takahashi')
