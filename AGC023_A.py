N=int(input())
A=list(map(int, input().split()))
S=[0]
ans=0
for i in range(len(A)):
  S.append(S[i] + A[i])
S.sort()
count = 1
for i in range(1, len(S)):
  if S[i-1] == S[i]:
    count += 1
  else:
    ans += count * (count-1) / 2
    count = 1
ans+=count*(count-1)/2
print(int(ans))
