r,d,x = map(int, input().split())
tmp = [x]
for i in range(1,11):
    tmp.append(tmp[i-1] * r - d)

del tmp[0]

for i in tmp:
    print(i)
