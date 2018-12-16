n=int(input())//2
a='b'
for i in range(1,n+1):
    if i%3==1:
        a='a'+a+'c'
    elif i%3==2:
        a='c'+a+'a'
    elif i%3==0:
        a='b'+a+'b'
print(['-1',n][a==input()])
