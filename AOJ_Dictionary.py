n=int(input())
dic=set()
for i in range(n):
    a,b=input().split()
    if a=="insert":
        dic.add(b)
    else:
        if b in dic:
            print("yes")
        else:
            print("no")
