a=int(input())
b=int(input())
normal=abs(b-a)
ans=normal
if normal>5:
    ans=10-normal
print(ans)
