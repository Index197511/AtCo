a,b=map(int,input().split());print(["Impossible","Possible"][a%3==0 or b%3==0 or (a+b)%3==0])
