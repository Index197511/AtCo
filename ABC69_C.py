n=int(input())
a=list(map(int,input().split()));tmp=[i%4 for i in a]
four=tmp.count(0)
two=tmp.count(2)
print(["No","Yes"][(four+two//2)>=len(a)//2])
