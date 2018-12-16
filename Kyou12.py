ans=[]
ans2=[]
n=int(input())
a=n//100
b=(n-a*100)//10
c=n-a*100-b*10
ans.append(a)
ans.append(b)
ans.append(c)
for i in ans:
    if i==1:
        ans2.append(str(9))
    else:
        ans2.append(str(1))
print(''.join(ans2))
