n,m=map(int,input().split())
if n>=12:
    n=n-12
minute_hand=float(m*6)
short_hand=float(n*30+m*0.5)
if abs(minute_hand-short_hand)>=180:
    print(360-abs(minute_hand-short_hand))
else:
    print(abs(minute_hand-short_hand))
