n=int(input())
if n%2==0:
    print(int((n-2)*(1+(n-2)/2)))
if n%2==1:
    print(int(int((n-3)*(1+(n-3)/2)))+1)
