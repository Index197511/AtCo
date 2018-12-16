import sys
w=input()
for i in range(len(w)):
    if w.count(w[i])%2==0:
        pass
    else:
        print('No')
        sys.exit()
print('Yes')
