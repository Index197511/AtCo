import sys
m=float(input())
m/=1000
if m<0.1:
    print('00')
    sys.exit()
elif m<=5:
    if m<1:
        ans=m*10
        print('{}{}'.format(0,int(ans)))
        sys.exit()
    else:
        ans=m*10

elif m<=30:
    ans=m+50

elif m<=70:
    ans=(m-30)/5+80

else:
    ans=89


print('{}'.format(int(ans)))
