import math
import sys
tx,ty,tx2,ty2,dist,spe=map(int,input().split())
n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    distance=math.sqrt(abs(x-tx)**2+(y-ty)**2)+math.sqrt(abs(tx2-x)**2+(ty2-y)**2)
    if distance<=(spe*dist):
        print('YES')
        sys.exit()
print('NO')
