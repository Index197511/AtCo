s=input()
while len(s)>0:
    if s[-5:]=='dream' or s[-5:]=='erase':
        s=s[:len(s)-5]
        continue
    if s[-7:]=='dreamer':
        s=s[:len(s)-7]
        continue
    if s[-6:]=='eraser':
        s=s[:len(s)-6]
        continue
    print('NO')
    break
else:
    print('YES')
