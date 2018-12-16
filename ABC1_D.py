n=int(input())
imos=[0]*1440
start=100000
end=0
sta=[]
end=[]
fr1=0
en1=0
fr2=0
en2=0
for i in range(n):
    a,b=input().split('-')
    a=int(a)
    b=int(b)
    a=(a%100)+(a-a%100)/100*60
    b=(b%100)+(b-b%100)/100*60
    a=a-(a%5)
    b=b+(5-(b%5))
    a=int(a)
    b=int(b)
    imos[a]+=1
    imos[b+1]-=1
for i in range(1,1440):
    imos[i]+=imos[i-1]
for i in range(1440):
    if imos[i]>0:
        start=min(start,i)
        sta.append(start)
        for j in range(i,1440):
            if imos[j]==0:
                end.append(j)
                break
for i in range(len(sta)):
    fr1=sta[i]//60
    en1=sta[i]%60
    fr2=end[i]//60
    en2=end[i]%60
    print('{}{}-{}{}'.format(fr1,en1,fr2,en2))
