s=input()
cnt=0
for i in range(len(s)):
    if i==len(s)-1:
        pass
    else:
        if s[i]!=s[i+1]:
            cnt+=1
print(cnt)
