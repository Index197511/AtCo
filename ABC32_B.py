s=input()
k=int(input())
an=set({})
for i in range(len(s)-k+1):
    an.add(s[i:i+k])
print(len(an))
