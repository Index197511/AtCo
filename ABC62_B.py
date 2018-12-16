h,w=map(int,input().split())
tmp=[]
for i in range(h):
    tmp.append(input())
for i in range(h+2):
    if i==0:
        a="#"*(w+2)
        print(a)
    elif i==(h+1):
        a="#"*(w+2)
        print(a)
    else:
        print("#{}#".format(tmp[i-1]))
