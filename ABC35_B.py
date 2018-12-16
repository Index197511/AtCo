s=input()
t=int(input())
a=abs(s.count('U')-s.count('D'))+abs(s.count('L')-s.count('R'))
b=s.count('?')
if t==1:
    print(a+b)
else:
    if a>b:
        print(a-b)
    else:
        b-=a
        a=b%2
        print(a)
