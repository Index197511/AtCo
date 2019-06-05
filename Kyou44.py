n,m = map(int, input().split())
a = list(map(int,input().split()))
a.sort()
ans = 0
tmp = []
tm = 0
for i in range(m):
    cnt = 0
    b,c = map(int, input().split())
    tmp.append([b,c])

tmp = sorted(tmp, reverse = True, key = lambda x : x[1])
cnt = 0
for i in range(n):
    if a[i] < tmp[cnt][1]:
        a[i] = tmp[cnt][1]
        tmp[cnt][0] -= 1
        if tmp[cnt][0] == 0:
            cnt += 1
            if cnt == m:
                break
    else:
        break

print(sum(a))
