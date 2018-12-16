import sys
S=input()
T=input()
length=len(S)
for i in range(length):
    if S[i]==T[i]:
        pass
    elif S[i]=='@':
        if T[i] in ['a','t','c','o','d','e','r']:
            pass
        else:
            print('You will lose')
            sys.exit()
    elif T[i]=='@':
        if S[i] in ['a','t','c','o','d','e','r']:
            pass
        else:
            print('You will lose')
            sys.exit()
    else:
        print('You will lose')
        sys.exit()
print('You can win')
