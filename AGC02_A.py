a,b=map(int,input().split())
if (a>0 and b>0):
    print("Positive")
elif a==0 or b==0 or a==b:
    print("Zero")
elif a<0 and b<0:
    tmp=abs(a)-abs(b)+1
    if tmp%2==0:
        print("Positive")
    else:
        print("Negative")
else:
    print("Zero")
