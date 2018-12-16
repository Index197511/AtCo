import sys
s=list(input())
if s[0]!='A':
    print("WA")
    sys.exit()
else:
    s.remove("A")
x=s[1:-1]
if x.count('C')==1:
    s.remove('C')
else:
    print("WA")
    sys.exit()
a=''.join(s)
print(["WA","YES"][a.islower()])
