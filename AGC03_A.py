s=list(input())
if s.count('W')>0 and s.count('E')>0 and s.count('N')>0 and s.count('S')>0:
    print("Yes")
elif s.count('W')>0 and s.count('E')>0 and s.count('N')==0 and s.count('S')==0:
    print('Yes')
elif s.count('W')==0 and s.count('E')==0 and s.count('N')>0 and s.count('S')>0:
    print('Yes')
else:
    print("No")
