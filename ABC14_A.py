import sys
a=int(input())
b=int(input())
for i in range(100):
    if (a+i)%b==0:
        print(i)
        sys.exit()
