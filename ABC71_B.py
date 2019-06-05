s=input()
tmp="abcdefghijklmnopqrstuvwxyz"
if len(set(s))==26:
    print("None")
    exit()
for i in tmp:
    if not i in s:
        print(i)
        break
