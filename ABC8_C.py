
n = int(input())
c = [int(input()) for i in range(n)]
c = sorted(c)
answer = 0
for i in range(n):
	num = 0
	for j in range(n):
		if c[i]<c[j]: break
		if i!=j and c[i]%c[j]==0: num+=1
	if num==0: answer+=1
	elif num%2==1: answer+=0.5
	else: answer+=(num+2)*1.0/(num*2+2)
print(answer)
