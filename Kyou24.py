a,b,k=map(int,input().split())
tmp=0
cnt=0
for i in range(k):
    if a%2!=0:
        a=a-1
    else:
        pass
    tmp=a//2
    a=a//2
    b=b+tmp
    cnt+=1

    if cnt>=k:
        break
    if b%2!=0:
        b=b-1
    else:
        pass
    tmp=b//2
    b=b//2
    a+=tmp
    cnt+=1

    if cnt>=k:
        break

print('{} {}'.format(int(a),int(b)))
