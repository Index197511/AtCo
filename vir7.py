import sys
a=int(input())
b=int(input())
n=int(input())
for i in range(n,n+a*b):
    if i%a<1 and i%b<1:
        print(i)
        sys.exit()
