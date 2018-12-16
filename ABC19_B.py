s=input()
an=[]
line=[]
cnt=1
for i in range(len(s)):
    if i==len(s)-1:
        an.append(cnt)
        memo=s[i]+str(cnt)
        line.append(memo)
        cnt=int(cnt)
        cnt=1
        break
    if s[i]==s[i+1]:
        cnt+=1
    else:
        an.append(cnt)
        memo=s[i]+str(cnt)
        line.append(memo)
        cnt=int(cnt)
        cnt=1
print(''.join(line))
